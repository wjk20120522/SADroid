#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Androguard.
#
# Copyright (C) 2012, Anthony Desnos <desnos at t0t0.fr>
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from androguard.core import bytecode
from androguard.core import androconf
from androguard.core.bytecodes.dvm_permissions import DVM_PERMISSIONS
from androguard.util import read

import StringIO
from struct import pack, unpack
from xml.sax.saxutils import escape
from zlib import crc32
import re
import os

from xml.dom import minidom

NS_ANDROID_URI = 'http://schemas.android.com/apk/res/android'


######################################################## APK FORMAT ########################################################

class APK(object):
    """
        This class can access to all elements in an APK file
        :param filename: specify the path of the file
        :type filename: string
    """

    def __init__(self, filename):

        self.filename = filename

        self.xml = {}
        self.axml = {}

        self.package = ''
        self.androidversion = {}
        self.permissions = []
        self.no_duplicate_permission = []
        self.declared_permissions = {}
        self.valid_apk = False
        # find onClick function and Button id in layout xml files
        self.xmlcallbacks = []

        self.__raw = read(filename)

        import zipfile
        try:
            self.zip = zipfile.ZipFile(StringIO.StringIO(self.__raw))
        except IOError:
            return

        for i in self.zip.namelist():
            if i == 'AndroidManifest.xml':
                self.axml[i] = AXMLPrinter(self.zip.read(i))
                try:
                    self.xml[i] = minidom.parseString(self.axml[i].get_buff())
                except IOError:
                    self.xml[i] = None
                if self.xml[i]:
                    self.package = self.xml[i].documentElement.getAttribute('package')
                    self.androidversion['Code'] = \
                        self.xml[i].documentElement.getAttributeNS(NS_ANDROID_URI, 'versionCode')
                    self.androidversion['Name'] = \
                        self.xml[i].documentElement.getAttributeNS(NS_ANDROID_URI, 'versionName')
                    for item in self.xml[i].getElementsByTagName('uses-permission'):
                        self.permissions.append(str(item.getAttributeNS(NS_ANDROID_URI, 'name')))

                    # getting details of the declared permissions
                    for d_perm_item in self.xml[i].getElementsByTagName('permission'):
                        d_perm_name = self._get_res_string_value(str(
                            d_perm_item.getAttributeNS(NS_ANDROID_URI, "name")))
                        d_perm_label = self._get_res_string_value(str(
                            d_perm_item.getAttributeNS(NS_ANDROID_URI, "label")))
                        d_perm_description = self._get_res_string_value(str(
                            d_perm_item.getAttributeNS(NS_ANDROID_URI, "description")))
                        d_perm_permission_group = self._get_res_string_value(str(
                            d_perm_item.getAttributeNS(NS_ANDROID_URI, "permissionGroup")))
                        d_perm_protection_level = self._get_res_string_value(str(
                            d_perm_item.getAttributeNS(NS_ANDROID_URI, "protectionLevel")))

                        d_perm_details = {
                            "label": d_perm_label,
                            "description": d_perm_description,
                            "permissionGroup": d_perm_permission_group,
                            "protectionLevel": d_perm_protection_level,
                        }
                        self.declared_permissions[d_perm_name] = d_perm_details

                    self.valid_apk = True

            elif i.find("res/layout/") != -1:   # find the onClick callback method in layout xml
                try:
                    xml = minidom.parseString(AXMLPrinter(self.zip.read(i)).get_buff())
                    for item in xml.getElementsByTagName("Button"):
                            callback = item.getAttributeNS(NS_ANDROID_URI, 'onClick')
                            buttonid = item.getAttributeNS(NS_ANDROID_URI, 'id')
                            if callback != "" and buttonid != "":
                                self.xmlcallbacks.append([buttonid, callback])
                except IOError:
                    pass

    def _get_res_string_value(self, string):
        if not string.startswith('@string/'):
            return string
        string_key = string[9:]

        res_parser = self.get_android_resources()
        string_value = ''
        for package_name in res_parser.get_packages_names():
            extracted_values = res_parser.get_string(package_name, string_key)
            if extracted_values:
                string_value = extracted_values[1]
                break
        return string_value

    def get_information_about_apk(self):

        info = '<?xml version="1.0" encoding="UTF-8"?>\n'

        # root tag
        info += '<apk>\n'
        info += '<package name = "%s">\n' % self.package
        info += '</package>\n'
        info += '<use-permission> \n'
        for permission in self.get_no_duplicate_permission():
            info += '<permission name = "%s">\n ' % permission
            info += '</permission>\n'

        info += '</use-permission> \n'
        info += '</apk>'
        return info

    def get_androidmanifest(self):
        """
            Return the Android Manifest XML file
            :rtype: xml object
        """
        return self.xml['AndroidManifest.xml']

    def is_valid_apk(self):
        """
            Return true if the APK is valid, false otherwise
            :rtype: boolean
        """
        return self.valid_apk

    def get_package(self):
        """
            Return the name of the package
            :rtype: string
        """
        return self.package

    def get_androidversion_code(self):
        """
            Return the android version code
            :rtype: string
        """
        return self.androidversion['Code']

    def get_androidversion_name(self):
        """
            Return the android version name
            :rtype: string
        """
        return self.androidversion['Name']

    def get_dex(self):
        """
        :return: dex file
        """
        return self.get_file('classes.dex')

    def get_files(self):
        """
            Return the files inside the APK
            :rtype: a list of strings
        """
        return self.zip.namelist()

    def get_file(self, filename):
        """
            Return the raw data of the specified filename
            :param filename a string which specify the filename
            :rtype: string
        """
        try:
            return self.zip.read(filename)
        except KeyError:
            return ''

    def get_elements(self, tag_name, attribute):
        """
            Return elements in xml files which match with the tag name and the specific attribute
            :param tag_name: a string which specify the tag name
            :param attribute: a string which specify the attribute
        """
        l = []
        for i in self.xml:
            for item in self.xml[i].getElementsByTagName(tag_name):
                value = item.getAttributeNS(NS_ANDROID_URI, attribute)
                value = self.format_value(value)
                l.append(str(value))
        return l

    def format_value(self, value):
        if len(value) > 0x0000:
            if value[0x0000] == '.':
                value = self.package + value
            elif value.find('.') == -0x0001:
                value = self.package + '.' + value
        return value

    def get_element(self, tag_name, attribute):
        """
            Return element in xml files which match with the tag name and the specific attribute
            :param tag_name: specify the tag name
            :type tag_name: string
            :param attribute: specify the attribute
            :type attribute: string
            :rtype: string
        """
        for i in self.xml:
            for item in self.xml[i].getElementsByTagName(tag_name):
                value = item.getAttributeNS(NS_ANDROID_URI, attribute)
                if len(value) > 0x0000:
                    return value
        return None

    def get_main_activity(self):
        """
            Return the name of the main activity
            :rtype: string
        """
        x = set()
        y = set()
        for i in self.xml:
            for item in self.xml[i].getElementsByTagName('activity'):
                for sitem in item.getElementsByTagName('action'):
                    val = sitem.getAttributeNS(NS_ANDROID_URI, 'name')
                    if val == 'android.intent.action.MAIN':
                        x.add(item.getAttributeNS(NS_ANDROID_URI, 'name'))
                for sitem in item.getElementsByTagName('category'):
                    val = sitem.getAttributeNS(NS_ANDROID_URI, 'name')
                    if val == 'android.intent.category.LAUNCHER':
                        y.add(item.getAttributeNS(NS_ANDROID_URI, 'name'))
        z = x.intersection(y)
        if len(z) > 0x0000:
            return self.format_value(z.pop())
        return None

    def get_activities(self):
        """
            Return the android:name attribute of all activities
            :rtype: a list of string
        """
        return self.get_elements('activity', 'name')

    def get_services(self):
        """
            Return the android:name attribute of all services
            :rtype: a list of string
        """
        return self.get_elements('service', 'name')

    def get_receivers(self):
        """
            Return the android:name attribute of all receivers
            :rtype: a list of string
        """
        return self.get_elements('receiver', 'name')

    def get_providers(self):
        """
            Return the android:name attribute of all providers
            :rtype: a list of string
        """
        return self.get_elements('provider', 'name')

    def get_actions(self):      # for risk evaluation
        actions = self.get_elements('action', 'name')
        res = []
        for action in actions:
            if action not in res:
                res.append(action)
        return res

    def get_system_actions(self):   # for risk evaluation
        actions = []
        for action in self.get_actions():
            if action.find('android') == 0:
                actions.append(action)
        return actions

    def get_intent_filters(self, category, name):
        d = {}

        d['action'] = []
        d['category'] = []

        for i in self.xml:
            for item in self.xml[i].getElementsByTagName(category):
                if self.format_value(item.getAttributeNS(NS_ANDROID_URI,
                        'name')) == name:
                    for sitem in \
                        item.getElementsByTagName('intent-filter'):
                        for ssitem in \
                            sitem.getElementsByTagName('action'):
                            if ssitem.getAttributeNS(NS_ANDROID_URI,
                                    'name') not in d['action']:

                                d['action'
                                  ].append(ssitem.getAttributeNS(NS_ANDROID_URI,
                                        'name'))
                        for ssitem in \
                            sitem.getElementsByTagName('category'):
                            if ssitem.getAttributeNS(NS_ANDROID_URI,
                                    'name') not in d['category']:

                                d['category'
                                  ].append(ssitem.getAttributeNS(NS_ANDROID_URI,
                                        'name'))

        if not d['action']:
            del d['action']

        if not d['category']:
            del d['category']
        return d

    def get_permissions(self):
        """
            Return permissions
            :rtype: list of string
        """
        return self.permissions

    def get_no_duplicate_permission(self):
        """
        return permissions
        :return: list of string
        """
        for permission in self.permissions:
            if permission not in self.no_duplicate_permission:
                self.no_duplicate_permission.append(permission)
        return self.no_duplicate_permission

    def get_system_permission(self):
        no_duplicates = self.get_no_duplicate_permission()
        system_permissions = []
        for permission in no_duplicates:
            if permission.find("android.permission.") == 0 or permission.find("com.android.") == 0:
                system_permissions.append(permission)
        return system_permissions

    def get_details_permissions(self):
        """
            Return permissions with details
            :rtype: list of string
        """
        l = {}
        for i in self.permissions:
            try:
                l[i] = DVM_PERMISSIONS['MANIFEST_PERMISSION'][i]

            except KeyError:
                l[i] = ['normal',
                        'Unknown permission from android reference',
                        'Unknown permission from android reference']
        return l

    def get_max_sdk_version(self):
        """
            Return the android:maxSdkVersion attribute

            :rtype: string
        """

        return self.get_element('uses-sdk', 'maxSdkVersion')

    def get_min_sdk_version(self):
        """
            Return the android:minSdkVersion attribute

            :rtype: string
        """

        return self.get_element('uses-sdk', 'minSdkVersion')

    def get_target_sdk_version(self):
        """
            Return the android:targetSdkVersion attribute

            :rtype: string
        """

        return self.get_element('uses-sdk', 'targetSdkVersion')

    def get_libraries(self):
        """
            Return the android:name attributes for libraries

            :rtype: list
        """

        return self.get_elements('uses-library', 'name')

    def get_certificate(self, filename):
        """
            Return a certificate object by giving the name in the apk file
        """

        import chilkat

        cert = chilkat.CkCert()
        f = self.get_file(filename)
        data = chilkat.CkByteData()
        data.append2(f, len(f))
        success = cert.LoadFromBinary(data)
        return success, cert

    def new_zip(
        self,
        filename,
        deleted_files=None,
        new_files={},
        ):
        """
            Create a new zip file

            :param filename: the output filename of the zip
            :param deleted_files: a regex pattern to remove specific file
            :param new_files: a dictionnary of new files

            :type filename: string
            :type deleted_files: None or a string
            :type new_files: a dictionnary (key:filename, value:content of the file)
        """

        if self.zipmodule == 0x0002:
            from androguard.patch import zipfile
            zout = zipfile.ZipFile(filename, 'w')
        else:
            import zipfile
            zout = zipfile.ZipFile(filename, 'w')

        for item in self.zip.infolist():
            if deleted_files is not None:
                if re.match(deleted_files, item.filename) is None:
                    if item.filename in new_files:
                        zout.writestr(item, new_files[item.filename])
                    else:
                        buff = self.zip.read(item.filename)
                        zout.writestr(item, buff)
        zout.close()

    def get_android_manifest_axml(self):
        """
            Return the :class:`AXMLPrinter` object which corresponds to the AndroidManifest.xml file

            :rtype: :class:`AXMLPrinter`
        """

        try:
            return self.axml['AndroidManifest.xml']
        except KeyError:
            return None

    def get_android_manifest_xml(self):
        """
            Return the xml object which corresponds to the AndroidManifest.xml file

            :rtype: object
        """

        try:
            return self.xml['AndroidManifest.xml']
        except KeyError:
            return None

    def get_android_resources(self):
        """
            Return the :class:`ARSCParser` object which corresponds to the resources.arsc file

            :rtype: :class:`ARSCParser`
        """

        try:
            return self.arsc['resources.arsc']
        except KeyError:
            try:
                self.arsc['resources.arsc'] = \
                    ARSCParser(self.zip.read('resources.arsc'))
                return self.arsc['resources.arsc']
            except KeyError:
                return None

    def get_signature_name(self):
        signature_expr = re.compile("^(META-INF/)(.*)(\.RSA|\.DSA)$")
        for i in self.get_files():
            if signature_expr.search(i):
                return i
        return None

    def get_signature(self):
        signature_expr = re.compile("^(META-INF/)(.*)(\.RSA|\.DSA)$")
        for i in self.get_files():
            if signature_expr.search(i):
                return self.get_file(i)
        return None

    def show(self):
        print 'PERMISSIONS: '
        details_permissions = self.get_details_permissions()
        for i in details_permissions:
            print '\t', i, details_permissions[i]
        print 'MAIN ACTIVITY: ', self.get_main_activity()

        print 'ACTIVITIES: '
        activities = self.get_activities()
        for i in activities:
            filters = self.get_intent_filters('activity', i)
            print '\t', i, filters or ''

        print 'SERVICES: '
        services = self.get_services()
        for i in services:
            filters = self.get_intent_filters('service', i)
            print '\t', i, filters or ''

        print 'RECEIVERS: '
        receivers = self.get_receivers()
        for i in receivers:
            filters = self.get_intent_filters('receiver', i)
            print '\t', i, filters or ''

        print 'PROVIDERS: ', self.get_providers()


######################################################## AXML FORMAT ########################################################
# Translated from http://code.google.com/p/android4me/source/browse/src/android/content/res/AXmlResourceParser.java

UTF8_FLAG = 256

class StringBlock(object):

    def __init__(self, buff):
        self.start = buff.get_idx()
        self._cache = {}
        self.header = unpack('<h', buff.read(0x0002))[0x0000]
        self.header_size = unpack('<h', buff.read(0x0002))[0x0000]

        self.chunkSize = unpack('<i', buff.read(4))[0x0000]
        self.stringCount = unpack('<i', buff.read(4))[0x0000]
        self.styleOffsetCount = unpack('<i', buff.read(4))[0x0000]

        self.flags = unpack('<i', buff.read(4))[0x0000]
        self.m_isUTF8 = self.flags & UTF8_FLAG != 0x0000

        self.stringsOffset = unpack('<i', buff.read(4))[0x0000]
        self.stylesOffset = unpack('<i', buff.read(4))[0x0000]

        self.m_stringOffsets = []
        self.m_styleOffsets = []
        self.m_strings = []
        self.m_styles = []

        for i in range(0x0000, self.stringCount):
            self.m_stringOffsets.append(unpack('<i',
                    buff.read(4))[0x0000])

        for i in range(0x0000, self.styleOffsetCount):
            self.m_styleOffsets.append(unpack('<i',
                    buff.read(4))[0x0000])

        size = self.chunkSize - self.stringsOffset
        if self.stylesOffset != 0x0000:
            size = self.stylesOffset - self.stringsOffset

        # FIXME

        if size % 4 != 0x0000:
            androconf.warning('ooo')

        for i in range(0x0000, size):
            self.m_strings.append(unpack('=b',
                                  buff.read(0x0001))[0x0000])

        if self.stylesOffset != 0x0000:
            size = self.chunkSize - self.stylesOffset

            # FIXME

            if size % 4 != 0x0000:
                androconf.warning('ooo')

            for i in range(0x0000, size / 4):
                self.m_styles.append(unpack('<i', buff.read(4))[0x0000])

    def getString(self, idx):
        if idx in self._cache:
            return self._cache[idx]

        if idx < 0x0000 or not self.m_stringOffsets or idx \
            >= len(self.m_stringOffsets):
            return ''

        offset = self.m_stringOffsets[idx]

        if not self.m_isUTF8:
            length = self.getShort2(self.m_strings, offset)
            offset += 0x0002
            self._cache[idx] = self.decode(self.m_strings, offset,
                    length)
        else:
            offset += self.getVarint(self.m_strings, offset)[0x0001]
            varint = self.getVarint(self.m_strings, offset)

            offset += varint[0x0001]
            length = varint[0x0000]

            self._cache[idx] = self.decode2(self.m_strings, offset,
                    length)

        return self._cache[idx]

    def getStyle(self, idx):
        print idx
        print idx in self.m_styleOffsets, self.m_styleOffsets[idx]

        print self.m_styles[0x0000]

    def decode(
        self,
        array,
        offset,
        length,
        ):

        length = length * 0x0002
        length = length + length % 0x0002

        data = ''

        for i in range(0x0000, length):
            t_data = pack('=b', self.m_strings[offset + i])
            data += unicode(t_data, errors='ignore')
            if data[-0x0002:] == '\x00\x00':
                break

        end_zero = data.find('\x00\x00')
        if end_zero != -0x0001:
            data = data[:end_zero]

        return data.decode('utf-16', 'replace')

    def decode2(
        self,
        array,
        offset,
        length,
        ):

        data = ''

        for i in range(0x0000, length):
            t_data = pack('=b', self.m_strings[offset + i])
            data += unicode(t_data, errors='ignore')

        return data.decode('utf-8', 'replace')

    def getVarint(self, array, offset):
        val = array[offset]
        more = val & 0x80 != 0x0000
        val &= 0x7f

        if not more:
            return (val, 0x0001)
        return (val << 8 | array[offset + 0x0001] & 255, 0x0002)

    def getShort(self, array, offset):
        value = array[offset / 4]
        if offset % 4 / 0x0002 == 0x0000:
            return value & 65535
        else:
            return value >> 16

    def getShort2(self, array, offset):
        return (array[offset + 0x0001] & 255) << 8 | array[offset] & 255

    def show(self):
        print 'StringBlock', hex(self.start), hex(self.header), \
            hex(self.header_size), hex(self.chunkSize), \
            hex(self.stringsOffset), self.m_stringOffsets
        for i in range(0x0000, len(self.m_stringOffsets)):
            print i, repr(self.getString(i))


ATTRIBUTE_IX_NAMESPACE_URI = 0x0000
ATTRIBUTE_IX_NAME = 0x0001
ATTRIBUTE_IX_VALUE_STRING = 0x0002
ATTRIBUTE_IX_VALUE_TYPE = 0x0003
ATTRIBUTE_IX_VALUE_DATA = 4
ATTRIBUTE_LENGHT = 5

CHUNK_AXML_FILE = 0x00080003
CHUNK_RESOURCEIDS = 0x00080180
CHUNK_XML_FIRST = 0x00100100
CHUNK_XML_START_NAMESPACE = 0x00100100
CHUNK_XML_END_NAMESPACE = 0x00100101
CHUNK_XML_START_TAG = 0x00100102
CHUNK_XML_END_TAG = 0x00100103
CHUNK_XML_TEXT = 0x00100104
CHUNK_XML_LAST = 0x00100104

START_DOCUMENT = 0x0000
END_DOCUMENT = 0x0001
START_TAG = 0x0002
END_TAG = 0x0003
TEXT = 4


class AXMLParser(object):

    def __init__(self, raw_buff):
        self.reset()

        self.valid_axml = True
        self.buff = bytecode.BuffHandle(raw_buff)

        axml_file = unpack('<L', self.buff.read(4))[0x0000]

        if axml_file == CHUNK_AXML_FILE:
            self.buff.read(4)

            self.sb = StringBlock(self.buff)

            self.m_resourceIDs = []
            self.m_prefixuri = {}
            self.m_uriprefix = {}
            self.m_prefixuriL = []

            self.visited_ns = []
        else:
            self.valid_axml = False
            androconf.warning('Not a valid xml file')

    def is_valid(self):
        return self.valid_axml

    def reset(self):
        self.m_event = -0x0001
        self.m_lineNumber = -0x0001
        self.m_name = -0x0001
        self.m_namespaceUri = -0x0001
        self.m_attributes = []
        self.m_idAttribute = -0x0001
        self.m_classAttribute = -0x0001
        self.m_styleAttribute = -0x0001

    def next(self):
        self.doNext()
        return self.m_event

    def doNext(self):
        if self.m_event == END_DOCUMENT:
            return

        event = self.m_event

        self.reset()
        while True:
            chunkType = -0x0001

            # Fake END_DOCUMENT event.

            if event == END_TAG:
                pass

            # START_DOCUMENT

            if event == START_DOCUMENT:
                chunkType = CHUNK_XML_START_TAG
            else:
                if self.buff.end():
                    self.m_event = END_DOCUMENT
                    break
                chunkType = unpack('<L', self.buff.read(4))[0x0000]

            if chunkType == CHUNK_RESOURCEIDS:
                chunkSize = unpack('<L', self.buff.read(4))[0x0000]

                # FIXME

                if chunkSize < 8 or chunkSize % 4 != 0x0000:
                    androconf.warning('Invalid chunk size')

                for i in range(0x0000, chunkSize / 4 - 0x0002):
                    self.m_resourceIDs.append(unpack('<L',
                            self.buff.read(4))[0x0000])

                continue

            # FIXME

            if chunkType < CHUNK_XML_FIRST or chunkType \
                > CHUNK_XML_LAST:
                androconf.warning('invalid chunk type')

            # Fake START_DOCUMENT event.

            if chunkType == CHUNK_XML_START_TAG and event == -0x0001:
                self.m_event = START_DOCUMENT
                break

            self.buff.read(4)  # /*chunkSize*/
            lineNumber = unpack('<L', self.buff.read(4))[0x0000]
            self.buff.read(4)  # 0xFFFFFFFF

            if chunkType == CHUNK_XML_START_NAMESPACE or chunkType \
                == CHUNK_XML_END_NAMESPACE:
                if chunkType == CHUNK_XML_START_NAMESPACE:
                    prefix = unpack('<L', self.buff.read(4))[0x0000]
                    uri = unpack('<L', self.buff.read(4))[0x0000]

                    self.m_prefixuri[prefix] = uri
                    self.m_uriprefix[uri] = prefix
                    self.m_prefixuriL.append((prefix, uri))
                    self.ns = uri
                else:
                    self.ns = -0x0001
                    self.buff.read(4)
                    self.buff.read(4)
                    (prefix, uri) = self.m_prefixuriL.pop()

                    # del self.m_prefixuri[ prefix ]
                    # del self.m_uriprefix[ uri ]

                continue

            self.m_lineNumber = lineNumber

            if chunkType == CHUNK_XML_START_TAG:
                self.m_namespaceUri = unpack('<L',
                        self.buff.read(4))[0x0000]
                self.m_name = unpack('<L', self.buff.read(4))[0x0000]

                # FIXME

                self.buff.read(4)  # flags

                attributeCount = unpack('<L', self.buff.read(4))[0x0000]
                self.m_idAttribute = (attributeCount >> 16) - 0x0001
                attributeCount = attributeCount & 65535
                self.m_classAttribute = unpack('<L',
                        self.buff.read(4))[0x0000]
                self.m_styleAttribute = (self.m_classAttribute >> 16) \
                    - 0x0001

                self.m_classAttribute = (self.m_classAttribute & 65535) \
                    - 0x0001

                for i in range(0x0000, attributeCount
                               * ATTRIBUTE_LENGHT):
                    self.m_attributes.append(unpack('<L',
                            self.buff.read(4))[0x0000])

                for i in range(ATTRIBUTE_IX_VALUE_TYPE,
                               len(self.m_attributes),
                               ATTRIBUTE_LENGHT):
                    self.m_attributes[i] = self.m_attributes[i] >> 24

                self.m_event = START_TAG
                break

            if chunkType == CHUNK_XML_END_TAG:
                self.m_namespaceUri = unpack('<L',
                        self.buff.read(4))[0x0000]
                self.m_name = unpack('<L', self.buff.read(4))[0x0000]
                self.m_event = END_TAG
                break

            if chunkType == CHUNK_XML_TEXT:
                self.m_name = unpack('<L', self.buff.read(4))[0x0000]

                # FIXME

                self.buff.read(4)
                self.buff.read(4)

                self.m_event = TEXT
                break

    def getPrefixByUri(self, uri):
        try:
            return self.m_uriprefix[uri]
        except KeyError:
            return -0x0001

    def getPrefix(self):
        try:
            return self.sb.getString(self.m_uriprefix[self.m_namespaceUri])
        except KeyError:
            return u''

    def getName(self):
        if self.m_name == -0x0001 or self.m_event != START_TAG \
            and self.m_event != END_TAG:
            return u''

        return self.sb.getString(self.m_name)

    def getText(self):
        if self.m_name == -0x0001 or self.m_event != TEXT:
            return u''

        return self.sb.getString(self.m_name)

    def getNamespacePrefix(self, pos):
        prefix = self.m_prefixuriL[pos][0x0000]
        return self.sb.getString(prefix)

    def getNamespaceUri(self, pos):
        uri = self.m_prefixuriL[pos][0x0001]
        return self.sb.getString(uri)

    def getXMLNS(self):
        buff = ''
        for i in self.m_uriprefix:
            if i not in self.visited_ns:
                buff += 'xmlns:%s="%s"\n' \
                    % (self.sb.getString(self.m_uriprefix[i]),
                       self.sb.getString(self.m_prefixuri[self.m_uriprefix[i]]))
                self.visited_ns.append(i)
        return buff

    def getNamespaceCount(self, pos):
        pass

    def getAttributeOffset(self, index):

        # FIXME

        if self.m_event != START_TAG:
            androconf.warning('Current event is not START_TAG.')

        offset = index * 5

        # FIXME

        if offset >= len(self.m_attributes):
            androconf.warning('Invalid attribute index')

        return offset

    def getAttributeCount(self):
        if self.m_event != START_TAG:
            return -0x0001

        return len(self.m_attributes) / ATTRIBUTE_LENGHT

    def getAttributePrefix(self, index):
        offset = self.getAttributeOffset(index)
        uri = self.m_attributes[offset + ATTRIBUTE_IX_NAMESPACE_URI]

        prefix = self.getPrefixByUri(uri)

        if prefix == -0x0001:
            return ''

        return self.sb.getString(prefix)

    def getAttributeName(self, index):
        offset = self.getAttributeOffset(index)
        name = self.m_attributes[offset + ATTRIBUTE_IX_NAME]

        if name == -0x0001:
            return ''

        return self.sb.getString(name)

    def getAttributeValueType(self, index):
        offset = self.getAttributeOffset(index)
        return self.m_attributes[offset + ATTRIBUTE_IX_VALUE_TYPE]

    def getAttributeValueData(self, index):
        offset = self.getAttributeOffset(index)
        return self.m_attributes[offset + ATTRIBUTE_IX_VALUE_DATA]

    def getAttributeValue(self, index):
        offset = self.getAttributeOffset(index)
        valueType = self.m_attributes[offset + ATTRIBUTE_IX_VALUE_TYPE]
        if valueType == TYPE_STRING:
            valueString = self.m_attributes[offset
                    + ATTRIBUTE_IX_VALUE_STRING]
            return self.sb.getString(valueString)

        # WIP

        return ''


        # int valueData=m_attributes[offset+ATTRIBUTE_IX_VALUE_DATA];
        # return TypedValue.coerceToString(valueType,valueData);

TYPE_ATTRIBUTE = 0x0002
TYPE_DIMENSION = 5
TYPE_FIRST_COLOR_INT = 28
TYPE_FIRST_INT = 16
TYPE_FLOAT = 4
TYPE_FRACTION = 6
TYPE_INT_BOOLEAN = 18
TYPE_INT_COLOR_ARGB4 = 30
TYPE_INT_COLOR_ARGB8 = 28
TYPE_INT_COLOR_RGB4 = 31
TYPE_INT_COLOR_RGB8 = 29
TYPE_INT_DEC = 16
TYPE_INT_HEX = 17
TYPE_LAST_COLOR_INT = 31
TYPE_LAST_INT = 31
TYPE_NULL = 0x0000
TYPE_REFERENCE = 0x0001
TYPE_STRING = 0x0003

RADIX_MULTS = [0.00390625, 3.051758E-005, 1.192093E-007, 4.656613E-010]
DIMENSION_UNITS = [
    'px',
    'dip',
    'sp',
    'pt',
    'in',
    'mm',
    ]
FRACTION_UNITS = ['%', '%p']

COMPLEX_UNIT_MASK = 15


def complexToFloat(xcomplex):
    return float(xcomplex & 0xFFFFFF00) * RADIX_MULTS[xcomplex >> 4
            & 0x0003]


class AXMLPrinter(object):

    def __init__(self, raw_buff):
        self.axml = AXMLParser(raw_buff)
        self.xmlns = False

        self.buff = u''

        while True and self.axml.is_valid():
            _type = self.axml.next()

            if _type == START_DOCUMENT:
                self.buff += u'<?xml version="1.0" encoding="utf-8"?>\n'
            elif _type == START_TAG:
                self.buff += u'<' \
                    + self.getPrefix(self.axml.getPrefix()) \
                    + self.axml.getName() + u'\n'
                self.buff += self.axml.getXMLNS()

                for i in range(0x0000, self.axml.getAttributeCount()):
                    self.buff += '%s%s="%s"\n' \
                        % (self.getPrefix(self.axml.getAttributePrefix(i)),
                           self.axml.getAttributeName(i),
                           self._escape(self.getAttributeValue(i)))

                self.buff += u'>\n'
            elif _type == END_TAG:

                self.buff += '</%s%s>\n' \
                    % (self.getPrefix(self.axml.getPrefix()),
                       self.axml.getName())
            elif _type == TEXT:

                self.buff += '%s\n' % self.axml.getText()
            elif _type == END_DOCUMENT:
                break

    @staticmethod
    def _escape(s):
        s = s.replace('&', '&amp;')
        s = s.replace('"', '&quot;')
        s = s.replace("'", '&apos;')
        s = s.replace('<', '&lt;')
        s = s.replace('>', '&gt;')
        return escape(s)

    def get_buff(self):
        return self.buff.encode('utf-8')

    def get_xml(self):
        return minidom.parseString(self.get_buff()).toprettyxml(encoding='utf-8'
                )

    def get_xml_obj(self):
        return minidom.parseString(self.get_buff())

    @staticmethod
    def getPrefix(prefix):
        if prefix is None or len(prefix) == 0x0000:
            return u''
        return prefix + u':'

    def getAttributeValue(self, index):
        _type = self.axml.getAttributeValueType(index)
        _data = self.axml.getAttributeValueData(index)

        if _type == TYPE_STRING:
            return self.axml.getAttributeValue(index)
        elif _type == TYPE_ATTRIBUTE:

            return '?%s%08X' % (self.getPackage(_data), _data)
        elif _type == TYPE_REFERENCE:

            return '@%s%08X' % (self.getPackage(_data), _data)
        elif _type == TYPE_FLOAT:

            return '%f' % unpack('=f', pack('=L', _data))[0x0000]
        elif _type == TYPE_INT_HEX:

            return '0x%08X' % _data
        elif _type == TYPE_INT_BOOLEAN:

            if _data == 0x0000:
                return 'false'
            return 'true'
        elif _type == TYPE_DIMENSION:

            return '%f%s' % (complexToFloat(_data),
                             DIMENSION_UNITS[_data & COMPLEX_UNIT_MASK])
        elif _type == TYPE_FRACTION:

            return '%f%s' % (complexToFloat(_data) * 100,
                             FRACTION_UNITS[_data & COMPLEX_UNIT_MASK])
        elif TYPE_FIRST_COLOR_INT <= _type <= TYPE_LAST_COLOR_INT:
            return '#%08X' % _data
        elif TYPE_FIRST_INT <= _type <= TYPE_LAST_INT:
            return '%d' % androconf.long2int(_data)

        return '<0x%X, type 0x%02X>' % (_data, _type)

    @staticmethod
    def getPackage(ids):
        if ids >> 24 == 0x0001:
            return 'android:'
        return ''


RES_NULL_TYPE = 0x0000
RES_STRING_POOL_TYPE = 0x0001
RES_TABLE_TYPE = 0x0002
RES_XML_TYPE = 0x0003

# Chunk types in RES_XML_TYPE

RES_XML_FIRST_CHUNK_TYPE = 256
RES_XML_START_NAMESPACE_TYPE = 256
RES_XML_END_NAMESPACE_TYPE = 0x0101
RES_XML_START_ELEMENT_TYPE = 0x0102
RES_XML_END_ELEMENT_TYPE = 0x0103
RES_XML_CDATA_TYPE = 0x0104
RES_XML_LAST_CHUNK_TYPE = 0x017f

# This contains a uint32_t array mapping strings in the string
# pool back to resource identifiers.  It is optional.

RES_XML_RESOURCE_MAP_TYPE = 0x0180

# Chunk types in RES_TABLE_TYPE

RES_TABLE_PACKAGE_TYPE = 0x0200
RES_TABLE_TYPE_TYPE = 0x0201
RES_TABLE_TYPE_SPEC_TYPE = 0x0202


class ARSCParser(object):

    def __init__(self, raw_buff):
        self.analyzed = False
        self.buff = bytecode.BuffHandle(raw_buff)

        # print "SIZE", hex(self.buff.size())

        self.header = ARSCHeader(self.buff)
        self.packageCount = unpack('<i', self.buff.read(4))[0x0000]

        # print hex(self.packageCount)

        self.stringpool_main = StringBlock(self.buff)

        self.next_header = ARSCHeader(self.buff)
        self.packages = {}
        self.values = {}

        for i in range(0x0000, self.packageCount):
            current_package = ARSCResTablePackage(self.buff)
            package_name = current_package.get_name()

            self.packages[package_name] = []

            mTableStrings = StringBlock(self.buff)
            mKeyStrings = StringBlock(self.buff)

            # self.stringpool_main.show()
            # self.mTableStrings.show()
            # self.mKeyStrings.show()

            self.packages[package_name].append(current_package)
            self.packages[package_name].append(mTableStrings)
            self.packages[package_name].append(mKeyStrings)

            pc = PackageContext(current_package, self.stringpool_main,
                                mTableStrings, mKeyStrings)

            current = self.buff.get_idx()
            while not self.buff.end():
                header = ARSCHeader(self.buff)
                self.packages[package_name].append(header)

                if header.type == RES_TABLE_TYPE_SPEC_TYPE:
                    self.packages[package_name].append(ARSCResTypeSpec(self.buff,
                            pc))
                elif header.type == RES_TABLE_TYPE_TYPE:

                    a_res_type = ARSCResType(self.buff, pc)
                    self.packages[package_name].append(a_res_type)

                    entries = []
                    for i in range(0x0000, a_res_type.entryCount):
                        current_package.mResId = current_package.mResId \
                            & 0xffff0000 | i
                        entries.append((unpack('<i',
                                self.buff.read(4))[0x0000],
                                current_package.mResId))

                    self.packages[package_name].append(entries)

                    for (entry, res_id) in entries:
                        if self.buff.end():
                            break

                        if entry != -0x0001:
                            ate = ARSCResTableEntry(self.buff, res_id,
                                    pc)
                            self.packages[package_name].append(ate)
                elif header.type == RES_TABLE_PACKAGE_TYPE:

                    break
                else:
                    androconf.warning('unknown type')
                    break

                current += header.size
                self.buff.set_idx(current)

    def _analyse(self):
        if self.analyzed:
            return

        self.analyzed = True

        for package_name in self.packages:
            self.values[package_name] = {}

            nb = 0x0003
            for header in (self.packages[package_name])[nb:]:
                if isinstance(header, ARSCHeader):
                    if header.type == RES_TABLE_TYPE_TYPE:
                        a_res_type = self.packages[package_name][nb
                                + 0x0001]

                        if a_res_type.config.get_language() \
                            not in self.values[package_name]:
                            self.values[package_name][a_res_type.config.get_language()] = \
                                {}

                            self.values[package_name][a_res_type.config.get_language()]['public'
                                    ] = []

                        c_value = \
                            self.values[package_name][a_res_type.config.get_language()]

                        entries = self.packages[package_name][nb
                                + 0x0002]
                        nb_i = 0x0000
                        for (entry, res_id) in entries:
                            if entry != -0x0001:
                                ate = self.packages[package_name][nb
                                        + 0x0003 + nb_i]

                                # print ate.is_public(), a_res_type.get_type(), ate.get_value(), hex(ate.mResId)

                                if ate.get_index() != -0x0001:

                                    c_value['public'
        ].append((a_res_type.get_type(), ate.get_value(), ate.mResId))

                                if a_res_type.get_type() not in c_value:
                                    c_value[a_res_type.get_type()] = []

                                if a_res_type.get_type() == 'string':

                                    c_value['string'
        ].append(self.get_resource_string(ate))
                                elif a_res_type.get_type() == 'id':

                                    if not ate.is_complex():

                                        c_value['id'
        ].append(self.get_resource_id(ate))
                                elif a_res_type.get_type() == 'bool':

                                    if not ate.is_complex():

                                        c_value['bool'
        ].append(self.get_resource_bool(ate))
                                elif a_res_type.get_type() == 'integer':

                                    c_value['integer'
        ].append(self.get_resource_integer(ate))
                                elif a_res_type.get_type() == 'color':

                                    c_value['color'
        ].append(self.get_resource_color(ate))
                                elif a_res_type.get_type() == 'dimen':

                                    c_value['dimen'
        ].append(self.get_resource_dimen(ate))

                                # elif a_res_type.get_type() == "style":
                                #    c_value["style"].append(self.get_resource_style(ate))

                                nb_i += 0x0001
                nb += 0x0001

    def get_resource_string(self, ate):
        return [ate.get_value(), ate.get_key_data()]

    def get_resource_id(self, ate):
        x = [ate.get_value()]
        if ate.key.get_data() == 0x0000:
            x.append('false')
        elif ate.key.get_data() == 0x0001:
            x.append('true')
        return x

    def get_resource_bool(self, ate):
        x = [ate.get_value()]
        if ate.key.get_data() == 0x0000:
            x.append('false')
        elif ate.key.get_data() == -0x0001:
            x.append('true')
        return x

    def get_resource_integer(self, ate):
        return [ate.get_value(), ate.key.get_data()]

    def get_resource_color(self, ate):
        entry_data = ate.key.get_data()
        return [ate.get_value(), '#%02x%02x%02x%02x' % (entry_data
                >> 24 & 255, entry_data >> 16 & 255, entry_data >> 8
                & 255, entry_data & 255)]

    def get_resource_dimen(self, ate):
        try:
            return [ate.get_value(), '%s%s'
                    % (complexToFloat(ate.key.get_data()),
                    DIMENSION_UNITS[ate.key.get_data()
                    & COMPLEX_UNIT_MASK])]
        except Exception, why:
            androconf.warning(why.__str__())
            return [ate.get_value(), ate.key.get_data()]

    # FIXME

    def get_resource_style(self, ate):
        return ['', '']

    def get_packages_names(self):
        return self.packages.keys()

    def get_locales(self, package_name):
        self._analyse()
        return self.values[package_name].keys()

    def get_types(self, package_name, locale):
        self._analyse()
        return self.values[package_name][locale].keys()

    def get_public_resources(self, package_name, locale='\x00\x00'):
        self._analyse()

        buff = '<?xml version="1.0" encoding="utf-8"?>\n'
        buff += '<resources>\n'

        try:
            for i in self.values[package_name][locale]['public']:
                buff += '<public type="%s" name="%s" id="0x%08x" />\n' \
                    % (i[0x0000], i[0x0001], i[0x0002])
        except KeyError:
            pass

        buff += '</resources>\n'

        return buff.encode('utf-8')

    def get_string_resources(self, package_name, locale='\x00\x00'):
        self._analyse()

        buff = '<?xml version="1.0" encoding="utf-8"?>\n'
        buff += '<resources>\n'

        try:
            for i in self.values[package_name][locale]['string']:
                buff += '<string name="%s">%s</string>\n' % (i[0x0000],
                        i[0x0001])
        except KeyError:
            pass

        buff += '</resources>\n'

        return buff.encode('utf-8')

    def get_strings_resources(self):
        self._analyse()

        buff = '<?xml version="1.0" encoding="utf-8"?>\n'

        buff += '<packages>\n'
        for package_name in self.get_packages_names():
            buff += '<package name="%s">\n' % package_name

            for locale in self.get_locales(package_name):
                buff += '<locale value=%s>\n' % repr(locale)

                buff += '<resources>\n'
                try:
                    for i in self.values[package_name][locale]['string'
                            ]:
                        buff += '<string name="%s">%s</string>\n' \
                            % (i[0x0000], i[0x0001])
                except KeyError:
                    pass

                buff += '</resources>\n'
                buff += '</locale>\n'

            buff += '</package>\n'

        buff += '</packages>\n'

        return buff.encode('utf-8')

    def get_id_resources(self, package_name, locale='\x00\x00'):
        self._analyse()

        buff = '<?xml version="1.0" encoding="utf-8"?>\n'
        buff += '<resources>\n'

        try:
            for i in self.values[package_name][locale]['id']:
                if len(i) == 0x0001:
                    buff += '<item type="id" name="%s"/>\n' % i[0x0000]
                else:
                    buff += '<item type="id" name="%s">%s</item>\n' \
                        % (i[0x0000], i[0x0001])
        except KeyError:
            pass

        buff += '</resources>\n'

        return buff.encode('utf-8')

    def get_bool_resources(self, package_name, locale='\x00\x00'):
        self._analyse()

        buff = '<?xml version="1.0" encoding="utf-8"?>\n'
        buff += '<resources>\n'

        try:
            for i in self.values[package_name][locale]['bool']:
                buff += '<bool name="%s">%s</bool>\n' % (i[0x0000],
                        i[0x0001])
        except KeyError:
            pass

        buff += '</resources>\n'

        return buff.encode('utf-8')

    def get_integer_resources(self, package_name, locale='\x00\x00'):
        self._analyse()

        buff = '<?xml version="1.0" encoding="utf-8"?>\n'
        buff += '<resources>\n'

        try:
            for i in self.values[package_name][locale]['integer']:
                buff += '<integer name="%s">%s</integer>\n' \
                    % (i[0x0000], i[0x0001])
        except KeyError:
            pass

        buff += '</resources>\n'

        return buff.encode('utf-8')

    def get_color_resources(self, package_name, locale='\x00\x00'):
        self._analyse()

        buff = '<?xml version="1.0" encoding="utf-8"?>\n'
        buff += '<resources>\n'

        try:
            for i in self.values[package_name][locale]['color']:
                buff += '<color name="%s">%s</color>\n' % (i[0x0000],
                        i[0x0001])
        except KeyError:
            pass

        buff += '</resources>\n'

        return buff.encode('utf-8')

    def get_dimen_resources(self, package_name, locale='\x00\x00'):
        self._analyse()

        buff = '<?xml version="1.0" encoding="utf-8"?>\n'
        buff += '<resources>\n'

        try:
            for i in self.values[package_name][locale]['dimen']:
                buff += '<dimen name="%s">%s</dimen>\n' % (i[0x0000],
                        i[0x0001])
        except KeyError:
            pass

        buff += '</resources>\n'

        return buff.encode('utf-8')

    def get_id(
        self,
        package_name,
        rid,
        locale='\x00\x00',
        ):

        self._analyse()

        try:
            for i in self.values[package_name][locale]['public']:
                if i[0x0002] == rid:
                    return i
        except KeyError:
            return None

    def get_string(
        self,
        package_name,
        name,
        locale='\x00\x00',
        ):

        self._analyse()

        try:
            for i in self.values[package_name][locale]['string']:
                if i[0x0000] == name:
                    return i
        except KeyError:
            return None

    def get_items(self, package_name):
        self._analyse()
        return self.packages[package_name]


class PackageContext(object):

    def __init__(
        self,
        current_package,
        stringpool_main,
        mTableStrings,
        mKeyStrings,
        ):

        self.stringpool_main = stringpool_main
        self.mTableStrings = mTableStrings
        self.mKeyStrings = mKeyStrings
        self.current_package = current_package

    def get_mResId(self):
        return self.current_package.mResId

    def set_mResId(self, mResId):
        self.current_package.mResId = mResId


class ARSCHeader(object):

    def __init__(self, buff):
        self.start = buff.get_idx()
        self.type = unpack('<h', buff.read(0x0002))[0x0000]
        self.header_size = unpack('<h', buff.read(0x0002))[0x0000]
        self.size = unpack('<i', buff.read(4))[0x0000]


        # print "ARSCHeader", hex(self.start), hex(self.type), hex(self.header_size), hex(self.size)

class ARSCResTablePackage(object):

    def __init__(self, buff):
        self.start = buff.get_idx()
        self.id = unpack('<i', buff.read(4))[0x0000]
        self.name = buff.readNullString(256)
        self.typeStrings = unpack('<i', buff.read(4))[0x0000]
        self.lastPublicType = unpack('<i', buff.read(4))[0x0000]
        self.keyStrings = unpack('<i', buff.read(4))[0x0000]
        self.lastPublicKey = unpack('<i', buff.read(4))[0x0000]
        self.mResId = self.id << 24

        # print "ARSCResTablePackage", hex(self.start), hex(self.id), hex(self.mResId), repr(self.name.decode("utf-16", errors='replace')), hex(self.typeStrings), hex(self.lastPublicType), hex(self.keyStrings), hex(self.lastPublicKey)

    def get_name(self):
        name = self.name.decode('utf-16', 'replace')
        name = name[:name.find('\x00')]
        return name


class ARSCResTypeSpec(object):

    def __init__(self, buff, parent=None):
        self.start = buff.get_idx()
        self.parent = parent
        self.id = unpack('<b', buff.read(0x0001))[0x0000]
        self.res0 = unpack('<b', buff.read(0x0001))[0x0000]
        self.res1 = unpack('<h', buff.read(0x0002))[0x0000]
        self.entryCount = unpack('<i', buff.read(4))[0x0000]

        # print "ARSCResTypeSpec", hex(self.start), hex(self.id), hex(self.res0), hex(self.res1), hex(self.entryCount), "table:" + self.parent.mTableStrings.getString(self.id - 1)

        self.typespec_entries = []
        for i in range(0x0000, self.entryCount):
            self.typespec_entries.append(unpack('<i',
                    buff.read(4))[0x0000])


class ARSCResType(object):

    def __init__(self, buff, parent=None):
        self.start = buff.get_idx()
        self.parent = parent
        self.id = unpack('<b', buff.read(0x0001))[0x0000]
        self.res0 = unpack('<b', buff.read(0x0001))[0x0000]
        self.res1 = unpack('<h', buff.read(0x0002))[0x0000]
        self.entryCount = unpack('<i', buff.read(4))[0x0000]
        self.entriesStart = unpack('<i', buff.read(4))[0x0000]
        self.mResId = 0xff000000 & self.parent.get_mResId() | self.id \
            << 16
        self.parent.set_mResId(self.mResId)

        # print "ARSCResType", hex(self.start), hex(self.id), hex(self.res0), hex(self.res1), hex(self.entryCount), hex(self.entriesStart), hex(self.mResId), "table:" + self.parent.mTableStrings.getString(self.id - 1)

        self.config = ARSCResTableConfig(buff)

    def get_type(self):
        return self.parent.mTableStrings.getString(self.id - 0x0001)


class ARSCResTableConfig(object):

    def __init__(self, buff):
        self.start = buff.get_idx()
        self.size = unpack('<i', buff.read(4))[0x0000]
        self.imsi = unpack('<i', buff.read(4))[0x0000]
        self.locale = unpack('<i', buff.read(4))[0x0000]
        self.screenType = unpack('<i', buff.read(4))[0x0000]
        self.input = unpack('<i', buff.read(4))[0x0000]
        self.screenSize = unpack('<i', buff.read(4))[0x0000]
        self.version = unpack('<i', buff.read(4))[0x0000]

        self.screenConfig = 0x0000
        self.screenSizeDp = 0x0000

        if self.size >= 32:
            self.screenConfig = unpack('<i', buff.read(4))[0x0000]

            if self.size >= 36:
                self.screenSizeDp = unpack('<i', buff.read(4))[0x0000]

        self.exceedingSize = self.size - 36
        if self.exceedingSize > 0x0000:
            androconf.warning('too much bytes !')
            self.padding = buff.read(self.exceedingSize)

        # print "ARSCResTableConfig", hex(self.start), hex(self.size), hex(self.imsi), hex(self.locale), repr(self.get_language()), repr(self.get_country()), hex(self.screenType), hex(self.input), hex(self.screenSize), hex(self.version), hex(self.screenConfig), hex(self.screenSizeDp)

    def get_language(self):
        x = self.locale & 65535
        return chr(x & 255) + chr((x & 0xff00) >> 8)

    def get_country(self):
        x = (self.locale & 0xffff0000) >> 16
        return chr(x & 255) + chr((x & 0xff00) >> 8)


class ARSCResTableEntry(object):

    def __init__(
        self,
        buff,
        mResId,
        parent=None,
        ):

        self.start = buff.get_idx()
        self.mResId = mResId
        self.parent = parent
        self.size = unpack('<h', buff.read(0x0002))[0x0000]
        self.flags = unpack('<h', buff.read(0x0002))[0x0000]
        self.index = unpack('<i', buff.read(4))[0x0000]

        # print "ARSCResTableEntry", hex(self.start), hex(self.mResId), hex(self.size), hex(self.flags), hex(self.index), self.is_complex()#, hex(self.mResId)

        if self.flags & 0x0001:
            self.item = ARSCComplex(buff, parent)
        else:
            self.key = ARSCResStringPoolRef(buff, self.parent)

    def get_index(self):
        return self.index

    def get_value(self):
        return self.parent.mKeyStrings.getString(self.index)

    def get_key_data(self):
        return self.key.get_data_value()

    def is_public(self):
        return self.flags == 0x0000 or self.flags == 0x0002

    def is_complex(self):
        return self.flags & 0x0001 == 0x0001


class ARSCComplex(object):

    def __init__(self, buff, parent=None):
        self.start = buff.get_idx()
        self.parent = parent

        self.id_parent = unpack('<i', buff.read(4))[0x0000]
        self.count = unpack('<i', buff.read(4))[0x0000]

        self.items = []
        for i in range(0x0000, self.count):
            self.items.append((unpack('<i', buff.read(4))[0x0000],
                              ARSCResStringPoolRef(buff, self.parent)))


        # print "ARSCComplex", hex(self.start), self.id_parent, self.count, repr(self.parent.mKeyStrings.getString(self.id_parent))

class ARSCResStringPoolRef(object):

    def __init__(self, buff, parent=None):
        self.start = buff.get_idx()
        self.parent = parent

        self.skip_bytes = buff.read(0x0003)
        self.data_type = unpack('<b', buff.read(0x0001))[0x0000]
        self.data = unpack('<i', buff.read(4))[0x0000]

        # print "ARSCResStringPoolRef", hex(self.start), hex(self.data_type), hex(self.data)#, "key:" + self.parent.mKeyStrings.getString(self.index), self.parent.stringpool_main.getString(self.data)

    def get_data_value(self):
        return self.parent.stringpool_main.getString(self.data)

    def get_data(self):
        return self.data

    def get_data_type(self):
        return self.data_type


def get_arsc_info(arscobj):
    buff = ''
    for package in arscobj.get_packages_names():
        buff += package + ':\n'
        for locale in arscobj.get_locales(package):
            buff += '\t' + repr(locale) + ':\n'
            for ttype in arscobj.get_types(package, locale):
                buff += '\t\t' + ttype + ':\n'
                try:
                    tmp_buff = getattr(arscobj, 'get_' + ttype
                            + '_resources')(package,
                            locale).decode('utf-8', 'replace'
                            ).split('\n')
                    for i in tmp_buff:
                        buff += '\t\t\t' + i + '\n'
                except AttributeError:
                    pass
    return buff
