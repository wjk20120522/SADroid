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

import re, random, cPickle, collections
from androguard.core.androconf import error, warning, debug, \
    is_ascii_problem, load_api_specific_resource_module, framework_classes
from androguard.core.bytecodes import dvm

from androguard.core.bytecodes.api_permissions import DVM_PERMISSIONS_BY_PERMISSION, \
    DVM_PERMISSIONS_BY_ELEMENT
import os


class DVMBasicBlock(object):
    """
        A simple basic block of a dalvik method
    """

    def __init__(self, start, vm, method, context, framework_block=None):
        self.__vm = vm          # DalvikVMFormat
        self.method = method    # EncodedMethod
        self.context = context  # BasicBlocks

        self.last_length = 0
        self.nb_instructions = 0

        self.fathers = []
        self.childs = []

        self.start = start
        self.end = self.start

        self.special_ins = {}

        if framework_block:
            self.name = framework_block + '0x0000'
        else:
            self.name = '%s@0x%x' % (self.method.get_class_name()+self.method.get_name() +
                                     self.method.get_descriptor(), self.start)

        self.exception_analysis = None

        self.notes = []

    def get_notes(self):
        return self.notes

    def set_notes(self, value):
        self.notes = [value]

    def add_note(self, note):
        self.notes.append(note)

    def clear_notes(self):
        self.notes = []

    def get_instructions(self):
        """
            Get all instructions from a basic block.
            :rtype: Return all instructions in the current basic block
        """
        tmp_ins = []
        idx = 0
        if not self.method:         # for test
            return self.name
        for i in self.method.get_instructions():
            if self.start <= idx < self.end:
                tmp_ins.append(i)
            idx += i.get_length()
        return tmp_ins

    def get_instructions_output(self):
        ret = ""
        instructions = self.get_instructions()
        if isinstance(instructions, str):
            return instructions
        for instruction in instructions:
            if ret != "":
                ret += '\n'
            ret += instruction.get_output()
        return ret

    def get_nb_instructions(self):
        return self.nb_instructions

    def get_method(self):
        return self.method

    def get_name(self):
        return self.name
        # return '%s-BB@0x%x' % (self.method.get_name(), self.start)

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_last(self):
        return self.get_instructions()[-1]

    def get_next(self):
        """
            Get next basic blocks
            :rtype: a list of the next basic blocks
        """

        return self.childs

    def get_prev(self):
        """
            Get previous basic blocks
            :rtype: a list of the previous basic blocks
        """

        return self.fathers

    def set_fathers(self, f):
        self.fathers.append(f)

    def get_last_length(self):
        return self.last_length

    def set_childs(self, values):

        # print self, self.start, self.end, values
        if not values:
            next_block = self.context.get_basic_block(self.end + 1)
            if next_block is not None:
                self.childs.append((self.end - self.get_last_length(),
                                   self.end, next_block, 'intra'))
        else:
            for i in values:
                if i != -1:
                    next_block = self.context.get_basic_block(i)
                    if next_block is not None:
                        self.childs.append((self.end - self.get_last_length(),
                                            i, next_block, 'intra'))

        for c in self.childs:
            if c[2] is not None:
                c[2].set_fathers((c[1], c[0], self, 'intra'))

    def set_child(self, child):
        self.childs.append((0, 0, child, 'inter'))

    def push(self, i):
        self.nb_instructions += 1
        idx = self.end
        self.last_length = i.get_length()
        self.end += self.last_length

        op_value = i.get_op_value()

        if op_value == 0x26 or (0x2b <= op_value <= 0x2c):
            code = self.method.get_code().get_bc()
            self.special_ins[idx] = code.get_ins_off(idx + i.get_ref_off() * 2)

    def get_special_ins(self, idx):
        """
            Return the associated instruction to a specific instruction (for example a packed/sparse switch)

            :param idx: the index of the instruction

            :rtype: None or an Instruction
        """

        try:
            return self.special_ins[idx]
        except:
            return None

    def get_exception_analysis(self):
        return self.exception_analysis

    def set_exception_analysis(self, exception_analysis):
        self.exception_analysis = exception_analysis


class Enum(object):

    def __init__(self, names):
        self.names = names
        for value, name in enumerate(self.names):
            setattr(self, name.upper(), value)

    def tuples(self):
        return tuple(enumerate(self.names))


TAG_ANDROID = Enum(
    ['ANDROID', 'TELEPHONY', 'SMS', 'SMSMESSAGE', 'ACCESSIBILITYSERVICE',
     'ACCOUNTS', 'ANIMATION', 'APP', 'BLUETOOTH', 'CONTENT', 'DATABASE',
     'DEBUG', 'DRM', 'GESTURE', 'GRAPHICS', 'HARDWARE', 'INPUTMETHODSERVICE',
     'LOCATION', 'MEDIA', 'MTP', 'NET', 'NFC', 'OPENGL', 'OS', 'PREFERENCE',
     'PROVIDER', 'RENDERSCRIPT', 'SAX', 'SECURITY', 'SERVICE', 'SPEECH',
     'SUPPORT', 'TEST', 'TEXT', 'UTIL', 'VIEW', 'WEBKIT', 'WIDGET',
     'DALVIK_BYTECODE', 'DALVIK_SYSTEM', 'JAVA_REFLECTION'])


TAG_REVERSE_ANDROID = dict((i[0], i[1]) for i in TAG_ANDROID.tuples())

TAGS_ANDROID = {
    TAG_ANDROID.ANDROID: [0, "Landroid"],
    TAG_ANDROID.TELEPHONY: [0, "Landroid/telephony"],
    TAG_ANDROID.SMS: [0, "Landroid/telephony/SmsManager"],
    TAG_ANDROID.SMSMESSAGE: [0, "Landroid/telephony/SmsMessage"],
    TAG_ANDROID.DEBUG: [0, "Landroid/os/Debug"],
    TAG_ANDROID.ACCESSIBILITYSERVICE: [0, "Landroid/accessibilityservice"],
    TAG_ANDROID.ACCOUNTS: [0, "Landroid/accounts"],
    TAG_ANDROID.ANIMATION: [0, "Landroid/animation"],
    TAG_ANDROID.APP: [0, "Landroid/app"],
    TAG_ANDROID.BLUETOOTH: [0, "Landroid/bluetooth"],
    TAG_ANDROID.CONTENT: [0, "Landroid/content"],
    TAG_ANDROID.DATABASE: [0, "Landroid/database"],
    TAG_ANDROID.DRM: [0, "Landroid/drm"],
    TAG_ANDROID.GESTURE: [0, "Landroid/gesture"],
    TAG_ANDROID.GRAPHICS: [0, "Landroid/graphics"],
    TAG_ANDROID.HARDWARE: [0, "Landroid/hardware"],
    TAG_ANDROID.INPUTMETHODSERVICE: [0, "Landroid/inputmethodservice"],
    TAG_ANDROID.LOCATION: [0, "Landroid/location"],
    TAG_ANDROID.MEDIA: [0, "Landroid/media"],
    TAG_ANDROID.MTP: [0, "Landroid/mtp"],
    TAG_ANDROID.NET: [0, "Landroid/net"],
    TAG_ANDROID.NFC: [0, "Landroid/nfc"],
    TAG_ANDROID.OPENGL: [0, "Landroid/opengl"],
    TAG_ANDROID.OS: [0, "Landroid/os"],
    TAG_ANDROID.PREFERENCE: [0, "Landroid/preference"],
    TAG_ANDROID.PROVIDER: [0, "Landroid/provider"],
    TAG_ANDROID.RENDERSCRIPT: [0, "Landroid/renderscript"],
    TAG_ANDROID.SAX: [0, "Landroid/sax"],
    TAG_ANDROID.SECURITY: [0, "Landroid/security"],
    TAG_ANDROID.SERVICE: [0, "Landroid/service"],
    TAG_ANDROID.SPEECH: [0, "Landroid/speech"],
    TAG_ANDROID.SUPPORT: [0, "Landroid/support"],
    TAG_ANDROID.TEST: [0, "Landroid/test"],
    TAG_ANDROID.TEXT: [0, "Landroid/text"],
    TAG_ANDROID.UTIL: [0, "Landroid/util"],
    TAG_ANDROID.VIEW: [0, "Landroid/view"],
    TAG_ANDROID.WEBKIT: [0, "Landroid/webkit"],
    TAG_ANDROID.WIDGET: [0, "Landroid/widget"],
    TAG_ANDROID.DALVIK_BYTECODE: [0, "Ldalvik/bytecode"],
    TAG_ANDROID.DALVIK_SYSTEM: [0, "Ldalvik/system"],
    TAG_ANDROID.JAVA_REFLECTION: [0, "Ljava/lang/reflect"],
}


class Tags(object):
    """
      Handle specific tags

      :param patterns:
      :params reverse:
    """

    def __init__(self, patterns=TAGS_ANDROID, reverse=TAG_REVERSE_ANDROID):
        self.tags = set()

        self.patterns = patterns
        self.reverse = TAG_REVERSE_ANDROID

        for i in self.patterns:
            self.patterns[i][1] = re.compile(self.patterns[i][1])

    def emit(self, method):
        for i in self.patterns:
            if self.patterns[i][0] == 0:
                if self.patterns[i][1].search(method.get_class()) is not None:
                    self.tags.add(i)

    def emit_by_classname(self, classname):
        for i in self.patterns:
            if self.patterns[i][0] == 0:
                if self.patterns[i][1].search(classname) is not None:
                    self.tags.add(i)

    def get_list(self):
        return [self.reverse[i] for i in self.tags]

    def __contains__(self, key):
        return key in self.tags

    def __str__(self):
        return str([self.reverse[i] for i in self.tags])

    def empty(self):
        return self.tags == set()


class BasicBlocks(object):
    """
        This class represents all basic blocks of a method
    """

    def __init__(self):
        self.bb = []

    def push(self, bb):
        self.bb.append(bb)

    def pop(self, idx):
        return self.bb.pop(idx)

    def get_basic_block(self, idx):
        for i in self.bb:
            if i.get_start() <= idx < i.get_end():
                return i
        return None

    def get(self):
        """
            :rtype: return each basic block (:class:`DVMBasicBlock` object)
        """
        for i in self.bb:
            yield i

    def gets(self):
        """
            :rtype: a list of basic blocks (:class:`DVMBasicBlock` objects)
        """
        return self.bb

    def get_basic_block_pos(self, idx):
        return self.bb[idx]


class ExceptionAnalysis(object):

    def __init__(self, exception, bb):
        self.start = exception[0]
        self.end = exception[1]

        self.exceptions = exception[2:]

        for i in self.exceptions:
            i.append(bb.get_basic_block(i[1]))

    def show_buff(self):
        buff = '%x:%x\n' % (self.start, self.end)

        for i in self.exceptions:
            if i[2] is None:
                buff += '\t(%s -> %x %s)\n' % (i[0], i[1], i[2])
            else:
                buff += '\t(%s -> %x %s)\n' % (i[0], i[1], i[2].get_name())

        return buff[:-1]

    def get(self):
        d = {'start': self.start, 'end': self.end, 'list': []}

        for i in self.exceptions:
            d['list'].append({'name': i[0], 'idx': i[1], 'bb': i[2].get_name()})

        return d


class Exceptions(object):

    def __init__(self):
        self.exceptions = []

    def add(self, exceptions, basic_blocks):
        for i in exceptions:
            self.exceptions.append(ExceptionAnalysis(i, basic_blocks))

    def get_exception(self, addr_start, addr_end):
        for i in self.exceptions:

            if i.start >= addr_start and i.end <= addr_end:
                return i

            elif addr_end <= i.end and addr_start >= i.start:
                return i

        return None

    def gets(self):
        return self.exceptions

    def get(self):
        for i in self.exceptions:
            yield i


BasicOPCODES = []
for i in dvm.BRANCH_DVM_OPCODES:
    BasicOPCODES.append(re.compile(i))


class MethodAnalysis(object):
    """
        This class analyses in details a method of a class/dex file

        :type vm: a :class:`DalvikVMFormat` object
        :type method: a :class:`EncodedMethod` object
    """

    def __init__(self, vm, method):
        self.__vm = vm              # DalvikVMFormat
        self.method = method        # EncodedMethod

        self.basic_blocks = BasicBlocks()
        self.exceptions = Exceptions()
        self.frame_blocks = BasicBlocks()

        code = self.method.get_code()   # code:DalvikCode
        if code is None:
            return

        #################################################
        # intro-procedural control flow construction
        ################################################

        current_basic = DVMBasicBlock(0, self.__vm, self.method, self.basic_blocks)
        self.basic_blocks.push(current_basic)   # each element's type is DVMBasicBlock

        # bc is 'DCode' object
        bc = code.get_bc()
        l = []
        h = {}
        idx = 0

        debug('Parsing instructions')
        instructions = [i for i in bc.get_instructions()]
        for i in instructions:          # i : 'Instruction'
            for j in BasicOPCODES:      # branch
                if j.match(i.get_name()) is not None:
                    v = dvm.determine_next(i, idx, self.method)
                    h[idx] = v
                    l.extend(v)
                    break

            idx += i.get_length()

        debug('Parsing exceptions')
        excepts = dvm.determine_exception(self.__vm, self.method)
        for i in excepts:
            l.extend([i[0]])
            for handler in i[2:]:
                l.append(handler[1])

        debug("Creating basic blocks in %s" % self.method)
        idx = 0
        for i in instructions:
            # index is a destination
            if idx in l:
                if current_basic.get_nb_instructions() != 0:
                    current_basic = DVMBasicBlock(current_basic.get_end(),
                                                  self.__vm, self.method,
                                                  self.basic_blocks)
                    self.basic_blocks.push(current_basic)

            current_basic.push(i)

            # index is a branch instruction
            if idx in h:
                current_basic = DVMBasicBlock(current_basic.get_end(),
                                              self.__vm, self.method,
                                              self.basic_blocks)
                self.basic_blocks.push(current_basic)

            idx += i.get_length()

        if current_basic.get_nb_instructions() == 0:
            self.basic_blocks.pop(-1)

        debug('Settings basic blocks childs')

        for i in self.basic_blocks.get():
            try:
                i.set_childs(h[i.end - i.get_last_length()])
            except KeyError:
                i.set_childs([])

        debug('Creating exceptions')

        # Create exceptions
        self.exceptions.add(excepts, self.basic_blocks)

        for i in self.basic_blocks.get():
            # setup exception by basic block
            i.set_exception_analysis(self.exceptions.get_exception(i.start,
                                                                   i.end - 1))

        del instructions
        del h, l

    def method_call(self, off, method_analysis):
        from_block = self.basic_blocks.get_basic_block(off)
        to_block = method_analysis.basic_blocks.get_basic_block(0)
        if from_block and to_block:
            from_block.set_child(to_block)

    def method_call_framework(self, off, class_name, method_name, method_discriptor):
        from_block = self.basic_blocks.get_basic_block(off)
        to_block = DVMBasicBlock(0, None, None, None, class_name + method_name + method_discriptor)
        self.frame_blocks.bb.append(to_block)
        if from_block and to_block:
            from_block.set_child(to_block)

    def framework_call_method(self, method_analysis, class_name, method_name, method_disciptor):
        to_blcok = method_analysis.basic_blocks.get_basic_block(0)
        from_block = self.get_frame_block(class_name, method_name, method_disciptor)
        if from_block and to_block:
            from_block.set_child(to_blcok)

    def get_frame_block(self, class_name, method_name, method_discriptor):
        sig = class_name + method_name + method_discriptor
        for block in self.frame_blocks.bb:
            if block.name == sig + '0x0000':
                return block

    def get_basic_blocks(self):
        """
            :rtype: a :class:`BasicBlocks` object
        """
        return self.basic_blocks

    def get_length(self):
        """
            :rtype: an integer which is the length of the code
        """
        return self.get_code().get_length()     # TODO: buggy

    def get_vm(self):
        return self.__vm

    def get_method(self):
        return self.method

    def show(self):
        print 'METHOD', self.method.get_class_name(), \
            self.method.get_name(), self.method.get_descriptor()

        for i in self.basic_blocks.get():
            print '\t', i
            i.show()
            print ''

    def show_methods(self):
        print '\t #METHODS :'
        for i in self.__bb:
            methods = i.get_methods()
            for method in methods:
                print '\t\t-->', method.get_class_name(), \
                    method.get_name(), method.get_descriptor()
                for context in methods[method]:
                    print '\t\t\t |---|', context.details


class StringAnalysis(object):

    def __init__(self, value):
        self.value = value
        self.orig_value = value
        self.xreffrom = set()

    def AddXrefFrom(self, classobj, methodobj):
        #debug("Added strings xreffrom for %s to %s" % (self.value, methodobj))
        self.xreffrom.add((classobj, methodobj))

    def get_xref_from(self):
        return self.xreffrom

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_orig_value(self):
        return self.orig_value

    def __str__(self):
        data = "XREFto for string %s in\n" % repr(self.value)
        for ref_class, ref_method in self.xreffrom:
            data += "%s:%s\n" % (ref_class.get_vm_class().get_name(),
                                 ref_method)
        return data


class MethodClassAnalysis(object):

    def __init__(self, method):
        self.method = method
        self.xrefto = set()
        self.xreffrom = set()

    def AddXrefTo(self, classobj, methodobj, offset):
        #debug("Added method xrefto for %s [%s] to %s" % (self.method, classobj, methodobj))
        self.xrefto.add((classobj, methodobj, offset))

    def AddXrefFrom(self, classobj, methodobj, offset):
        #debug("Added method xreffrom for %s [%s] to %s" % (self.method, classobj, methodobj))
        self.xreffrom.add((classobj, methodobj, offset))

    def get_xref_from(self):
        return self.xreffrom

    def get_xref_to(self):
        return self.xrefto

    def __str__(self):
        data = "XREFto for %s\n" % self.method
        for ref_class, ref_method, offset in self.xrefto:
            data += "in\n"
            data += "%s:%s @0x%x\n" % (ref_class.get_vm_class().get_name(),
                                       ref_method, offset)

        data += "XREFFrom for %s\n" % self.method
        for ref_class, ref_method, offset in self.xreffrom:
            data += "in\n"
            data += "%s:%s @0x%x\n" % (ref_class.get_vm_class().get_name(),
                                       ref_method, offset)

        return data


class FieldClassAnalysis(object):

    def __init__(self, field):
        self.field = field
        self.xrefread = set()
        self.xrefwrite = set()

    def AddXrefRead(self, classobj, methodobj):
        #debug("Added method xrefto for %s [%s] to %s" % (self.method, classobj, methodobj))
        self.xrefread.add((classobj, methodobj))

    def AddXrefWrite(self, classobj, methodobj):
        #debug("Added method xreffrom for %s [%s] to %s" % (self.method, classobj, methodobj))
        self.xrefwrite.add((classobj, methodobj))

    def get_xref_read(self):
        return self.xrefread

    def get_xref_write(self):
        return self.xrefwrite

    def __str__(self):
        data = "XREFRead for %s\n" % self.field
        for ref_class, ref_method in self.xrefread:
            data += "in\n"
            data += "%s:%s\n" % (ref_class.get_vm_class().get_name(),
                                 ref_method)

        data += "XREFWrite for %s\n" % self.field
        for ref_class, ref_method in self.xrefwrite:
            data += "in\n"
            data += "%s:%s\n" % (ref_class.get_vm_class().get_name(),
                                 ref_method)

        return data


REF_NEW_INSTANCE = 0
REF_CLASS_USAGE = 1


class ClassAnalysis(object):

    def __init__(self, classobj):
        self.orig_class = classobj
        self.methods = {}
        self._fields = {}

        self.xrefto = collections.defaultdict(set)
        self.xreffrom = collections.defaultdict(set)

    def get_method_analysis(self, method):
        return self.methods.get(method)

    def get_field_analysis(self, field):
        return self._fields.get(field)

    def AddFXrefRead(self, method, classobj, field):
        if field not in self._fields:
            self._fields[field] = FieldClassAnalysis(field)
        self._fields[field].AddXrefRead(classobj, method)

    def AddFXrefWrite(self, method, classobj, field):
        if field not in self._fields:
            self._fields[field] = FieldClassAnalysis(field)
        self._fields[field].AddXrefWrite(classobj, method)

    def AddMXrefTo(self, method1, classobj, method2, offset):
        if method1 not in self.methods:
            self.methods[method1] = MethodClassAnalysis(method1)
        self.methods[method1].AddXrefTo(classobj, method2, offset)

    def AddMXrefFrom(self, method1, classobj, method2, offset):
        if method1 not in self.methods:
            self.methods[method1] = MethodClassAnalysis(method1)
        self.methods[method1].AddXrefFrom(classobj, method2, offset)

    def AddXrefTo(self, ref_kind, classobj, methodobj, offset):
        self.xrefto[classobj].add((ref_kind, methodobj, offset))

    def AddXrefFrom(self, ref_kind, classobj, methodobj, offset):
        self.xreffrom[classobj].add((ref_kind, methodobj, offset))

    def get_xref_from(self):
        return self.xreffrom

    def get_xref_to(self):
        return self.xrefto

    def get_vm_class(self):
        return self.orig_class

    def __str__(self):
        data = "XREFto for %s\n" % self.orig_class
        for ref_class in self.xrefto:
            data += str(ref_class.get_vm_class().get_name()) + " "
            data += "in\n"
            for ref_kind, ref_method, ref_offset in self.xrefto[ref_class]:
                data += "%d %s 0x%x\n" % (ref_kind, ref_method, ref_offset)

            data += "\n"

        data += "XREFFrom for %s\n" % self.orig_class
        for ref_class in self.xreffrom:
            data += str(ref_class.get_vm_class().get_name()) + " "
            data += "in\n"
            for ref_kind, ref_method, ref_offset in self.xreffrom[ref_class]:
                data += "%d %s 0x%x\n" % (ref_kind, ref_method, ref_offset)

            data += "\n"

        return data


class NewVmAnalysis(object):

    def __init__(self, vm):

        self.vms = [vm]
        self.classes = {}
        self.strings = {}
        self.methods = {}
        self.framework_classes = framework_classes
        self.framework_hierarchy_childs = {}
        # self.framework_hierarchy_parents = {}

        # self.class_hierarchy_framework = {}

        t = Test()
        t.get_class()
        t.parse_file_in_directory()

        for current_class in vm.get_classes():
            self.classes[current_class.get_name()] = ClassAnalysis(current_class)

    def non_framework_classes(self):
        for cl in self.classes.keys():
            if not self.framework_class(cl):
                print cl

    def get_class_nums(self):
        ret = 0
        for current_class in self.classes.keys():
            framework_class = False
            for framework in self.framework_classes:
                if current_class.find(framework) != -1:
                    framework_class = True
                    break
            if framework_class:
                continue
            ret += 1
        return ret

    def get_method_nums(self):
        ret = 0
        for vm in self.vms:
            ret += len(vm.get_methods())
        return ret

    def get_methods_nums_with_framework_class(self):
        ret = 0
        for vm in self.vms:
            ret += len(vm.get_methods_with_framework_class())
        return ret

    def intro_procedural_cfg(self):
        for vm in self.vms:
            for method in vm.get_methods(self.framework_classes):     # method : EncodedMethod
                self.methods[method] = MethodAnalysis(vm, method)

    def export_to_dot(self):
        buff = "digraph CFG {\n"
        # buff += self.generate_dot_edges_discription()
        buff += self.generate_dot_edges()
        buff += "\n}"
        return buff

    def generate_dot_edges_discription(self):
        buff = ""
        dots = set()
        edges = 0

        for vm in self.vms:
            for method in vm.get_methods(self.framework_classes):     # method : EncodedMethod
                g = self.methods[method]
                for i in g.basic_blocks.get():
                    instructions_begin = i.get_instructions_output()
                    dots.add(instructions_begin)
                    for j in i.childs:
                        if j[3] == 'inter':
                            edges += 1
                            dots.add(j[2].get_instructions_output())
                            instructions_end = j[2].get_instructions_output()
                            buff += '"' + instructions_begin + '"' + ' -> '
                            buff += '"' + instructions_end + '"'
                for i in g.frame_blocks.get():
                    instructions_begin = i.get_instructions_output()
                    dots.add(i.get_instructions_output())
                    for j in i.childs:
                        if j[3] == 'inter':
                            dots.add(j[2].get_instructions_output())
                            instructions_end = j[2].get_instructions_output()
                            buff += '"' + instructions_begin + '"' + ' -> '
                            buff += '"' + instructions_end + '"'
                            buff += '\n'
                            edges += 1

        for dot in dots:
            buff += '"' + dot + '"'
        buff += '\n'
        print "dots number: %d", len(dots)
        print "edges numbers: %d", edges
        return buff

    def generate_dot_edges(self):
        buff = ""
        dots = set()
        edges = 0

        for vm in self.vms:
            for method in vm.get_methods(self.framework_classes):     # method : EncodedMethod
                g = self.methods[method]
                for i in g.basic_blocks.get():
                    instructions_begin = i.name
                    dots.add(i.name)
                    for j in i.childs:
                        if j[3] == 'inter':
                            dots.add(j[2].name)
                            instructions_end = j[2].name
                            buff += '"' + instructions_begin + '"' + ' -> '
                            buff += '"' + instructions_end + '"'
                            edges += 1
                for i in g.frame_blocks.get():
                    instructions_begin = i.name
                    dots.add(i.name)
                    for j in i.childs:
                        if j[3] == 'inter':
                            dots.add(j[2].name)
                            instructions_end = j[2].name
                            buff += '"' + instructions_begin + '"' + ' -> '
                            buff += '"' + instructions_end + '"'
                            buff += '\n'
                            edges += 1

            '''
            for block in dots:
                    buff += '"' + block + '"' + '\n'
            '''

        '''
        for current_class in self.classes.keys():
            current_class_analysis = self.classes[current_class]
            for method in current_class_analysis.methods.keys():    # method -> EncodedMethod
                class_method_analysis = current_class_analysis.methods[method]
                for obj, met, off in class_method_analysis.xrefto:
                    if method.get_class_name().find("Landroid/support/") != -1 and met.get_class_name().find("Landroid/support/") != -1:
                        continue
                    m1 = method.get_class_name() + method.get_name() + method.get_descriptor()
                    m2 = met.get_class_name() + met.get_name() + met.get_descriptor()
                    dots.add(m1)
                    dots.add(m2)
                    buff += '"' + m1 + '"' + ' -> '
                    buff += '"' + m2 + '"'
                    buff += '\n'
                    edges += 1
        '''

        print "dots number: %d", len(dots)
        print "edges numbers: %d", edges
        return buff

    def framework_class(self, class_name):
        for framework_class in self.framework_classes:
            if class_name.find(framework_class) == 0:
                return True
        return False

    def explicit_icfg(self):
        #####################################################
        # explicit inter-procedural control flow construction
        #####################################################
        for vm in self.vms:
            for current_class in vm.get_classes():
                # 如果当前类是框架类,则直接跳过
                if self.framework_class(current_class.name):
                    continue
                for current_method in current_class.get_methods():
                    code = current_method.get_code()
                    if code is None:
                        continue
                    off = 0
                    bc = code.get_bc()
                    try:
                        for instruction in bc.get_instructions():
                            op_value = instruction.get_op_value()
                            # invoke-kind /range {vC, vD, vE, vF, vG}, meth@BBBB
                            if(0x6e <= op_value <= 0x72) or (0x74 <= op_value <= 0x78) or (0x22ff <= op_value <= 0x26ff):
                                # print instruction.get_output()
                                idx_meth = instruction.get_ref_kind()
                                method_info = vm.get_cm_method(idx_meth)
                                if method_info:
                                    # 如果调用的是框架层的代码
                                    if self.framework_class(method_info[0]):
                                        self.methods[current_method].method_call_framework(off, method_info[0],
                                                                                           method_info[1],
                                                                                           "".join(method_info[2]))
                                    else:
                                        destinate_class = method_info[0]
                                        destinate_method_name = method_info[1]
                                        destinate_method_discription = ''.join(method_info[2])
                                        # 代码中没有找到这样的调用函数
                                        if not vm.get_method_descriptor(destinate_class, destinate_method_name, destinate_method_discription):
                                            while not vm.get_method_descriptor(destinate_class, destinate_method_name, destinate_method_discription):
                                                if self.framework_class(destinate_class):
                                                    self.methods[current_method].method_call_framework(off, destinate_class,
                                                                                                       destinate_method_name,
                                                                                                       destinate_method_discription)
                                                    break
                                                else:
                                                    try:
                                                        destinate_class = vm.get_class(destinate_class).sname
                                                    except:
                                                        # print destinate_class
                                                        break

                                            # 当前的非框架类有这样的框架函数调用
                                            if not self.framework_class(destinate_class):
                                                self.methods[current_method].method_call_framework(off, destinate_class, destinate_method_name, destinate_method_discription)
                                        else:
                                            method_encode = vm.get_method_descriptor(destinate_class, destinate_method_name, destinate_method_discription)
                                            # 考虑多态
                                            org = [destinate_class]
                                            self.methods[current_method].method_call(off, self.methods[method_encode])
                                            while org:
                                                dst = []
                                                for c in org:
                                                    cur_class = vm.get_class(c)
                                                    if cur_class.childs_class_name:
                                                        for child_class in cur_class.childs_class_name:
                                                            method_encode = vm.get_method_descriptor(child_class, destinate_method_name, destinate_method_discription)
                                                            if method_encode:
                                                                self.methods[current_method].method_call(off, self.methods[method_encode])
                                                                dst.append(child_class)
                                                org = dst
                                else:
                                    pass
                                    # print 'do not find the specific method in smali. can not be here. '
                                    # exit('Look the bugs here in explicit_icfg construction')

                            off += instruction.get_length()
                    except dvm.InvalidInstruction as e:
                        warning("Invalid instruction %s" % str(e))

    def implicit_icfg(self, registration_callback):
        self.lifecycle_icfg()
        self.callback_icfg(registration_callback)
        pass

    def lifecycle_icfg(self):
        for vm in self.vms:
            for current_class in vm.get_classes():      # current_class : ClassDefItem
                if self.framework_class(current_class.name):
                    continue
                if self.activity_class(current_class.name, vm):
                    self.activity_lifecycle(current_class, vm)
                elif self.service_class(current_class.name, vm):
                    self.service_lifecycle(current_class, vm)
                elif self.broadcast_receiver_class(current_class.name, vm):
                    self.broadcast_receiver_lifecycle(current_class, vm)
                elif self.content_provider_class(current_class.name, vm):
                    self.content_provider_lifecycle(current_class, vm)

    def callback_icfg(self, registration_callback):
        for vm in self.vms:
            for current_class in vm.get_classes():
                if self.framework_class(current_class.name):
                    continue
                for current_method in current_class.get_methods():
                    code = current_method.get_code()
                    if code is None:
                        continue
                    off = 0
                    bc = code.get_bc()
                    try:
                        for instruction in bc.get_instructions():
                            op_value = instruction.get_op_value()
                            # invoke-kind /range {vC, vD, vE, vF, vG}, meth@BBBB
                            if(0x6e <= op_value <= 0x72) or (0x74 <= op_value <= 0x78) or (0x22ff <= op_value <= 0x26ff):
                                idx_meth = instruction.get_ref_kind()
                                method_info = vm.get_cm_method(idx_meth)
                                if method_info:
                                    from_class = method_info[0]
                                    from_method_name = method_info[1]
                                    from_method_discription = ''.join(method_info[2])

                                    while (from_class + '->' + from_method_name + from_method_discription) not in registration_callback.keys():
                                        if self.framework_class(from_class) and from_class.find("Landroid/support") == -1:
                                            try:
                                                from_class = class_hierarchy_framework[from_class[:-1] + '.java']['parents'][0]
                                                from_class = from_class[:-5] + ';'
                                            except:
                                                break
                                        else:
                                            try:
                                                from_class = vm.get_class(from_class).sname
                                            except:
                                                break

                                    signture = from_class + '->'+ from_method_name + from_method_discription
                                    # 如果存在这样的registration函数
                                    if signture in registration_callback.keys():
                                        reg = registration_callback[signture]
                                        for position in reg.keys():
                                            may_callback = reg[position]
                                            p1 = may_callback.find("->")
                                            p2 = may_callback.find("(")
                                            may_func = may_callback[p1+2:p2]

                                            if position == "0":
                                                # 当前类中存在着对应的回调函数
                                                method_encode = vm.get_method_descriptor(current_class.name, may_func, may_callback[p2:])
                                                if method_encode:
                                                    try:
                                                        self.methods[current_method].framework_call_method(self.methods[method_encode], method_info[0], method_info[1], ''.join(method_info[2]),)
                                                    except:
                                                        pass
                                                        # print method_info[0] + method_info[1] + ''.join(method_info[2])
                                            else:
                                                may_class = 'L' + may_callback[:p1]
                                                # print may_class
                                                if may_class in self.framework_hierarchy_childs.keys():
                                                    childs = self.framework_hierarchy_childs[may_class]
                                                    if childs:
                                                        dst = []
                                                        for child in childs:
                                                            method_encode = vm.get_method_descriptor(child, may_func, may_callback[p2:])
                                                            if method_encode:
                                                                try:
                                                                    self.methods[current_method].framework_call_method(self.methods[method_encode], method_info[0], method_info[1], ''.join(method_info[2]))
                                                                except:
                                                                    pass
                                                            else:
                                                                if child in self.framework_hierarchy_childs.keys():
                                                                    dst.append(child)
                                                        # childs = dst

                            off += instruction.get_length()
                    except dvm.InvalidInstruction as e:
                        warning("Invalid instruction %s" % str(e))

    def activity_lifecycle(self, current_class, vm):
        pass

    def service_lifecycle(self, current_class, vm):
        pass

    def broadcast_receiver_lifecycle(self, current_class, vm):
        pass

    def content_provider_lifecycle(self, current_class, vm):
        pass

    def activity_class(self, class_name, vm):
        return self.ancestor_class(class_name, "Landroid/app/Activity", vm)

    def service_class(self, class_name, vm):
        return self.ancestor_class(class_name, "Landroid.app.Service", vm)

    def broadcast_receiver_class(self, class_name, vm):
        return self.ancestor_class(class_name, "Landroid/content/BroadcastReceiver", vm)

    def content_provider_class(self, class_name, vm):
        return self.ancestor_class(class_name, "Landroid.content.ContentProvider", vm)

    def application_class(self, class_name, vm):
        return self.ancestor_class(class_name, "android.app.Application", vm)

    def ancestor_class(self, class_name, ancestor_name, vm):
        while class_name != ancestor_name:
            if self.framework_class(class_name):
                if class_name.find("Landroid/support") != -1:
                    if vm.get_class(class_name):
                        class_name = vm.get_class(class_name).sname
                    else:
                        return False
                else:
                    return False
            else:
                if vm.get_class(class_name):
                    class_name = vm.get_class(class_name).sname
                else:
                    return False
        return True

    # def find_corresponding_framework_class(self, class_name, vm):
    #     while not self.framework_class(class_name) or class_name.find("Landroid/support") != -1:
    #         class_name = vm.get_class(class_name).sname
    #     return class_name

    def create_xref(self):
        instances_class_name = self.classes.keys()

        for vm in self.vms:
            for current_class in vm.get_classes():
                if current_class.name.find("Landroid/support/") != -1:
                    continue
                for current_method in current_class.get_methods():
                    code = current_method.get_code()
                    if code is None:
                        continue
                    off = 0
                    bc = code.get_bc()
                    try:
                        for instruction in bc.get_instructions():
                            op_value = instruction.get_op_value()
                            if op_value in [0x1c, 0x22]:
                                idx_type = instruction.get_ref_kind()
                                type_info = vm.get_cm_type(idx_type)
                                # Internal class manipulation
                                if type_info in instances_class_name and type_info != current_class.get_name():
                                    # new-instance vAA, type@BBBB
                                    if op_value == 0x22:
                                        self.classes[current_class.get_name(
                                        )].AddXrefTo(REF_NEW_INSTANCE,
                                                     self.classes[type_info],
                                                     current_method, off)
                                        self.classes[type_info].AddXrefFrom(
                                            REF_NEW_INSTANCE,
                                            self.classes[current_class.get_name()],
                                            current_method, off)
                                    # const-class vAA, type@BBBB
                                    else:
                                        self.classes[current_class.get_name()].AddXrefTo(REF_CLASS_USAGE,
                                                                                         self.classes[type_info],
                                                                                         current_method, off)
                                        self.classes[type_info].AddXrefFrom(REF_CLASS_USAGE,
                                                                            self.classes[current_class.get_name()],
                                                                            current_method, off)

                            # invoke-kind /range {vC, vD, vE, vF, vG}, meth@BBBB
                            elif (0x6e <= op_value <= 0x72) or (0x74 <= op_value <= 0x78):
                                idx_meth = instruction.get_ref_kind()
                                method_info = vm.get_cm_method(idx_meth)
                                if method_info:
                                    class_info = method_info[0]

                                    method_item = vm.get_method_descriptor(
                                        method_info[0], method_info[1],
                                        ''.join(method_info[2]))
                                    if method_item:
                                        self.classes[current_class.get_name(
                                        )].AddMXrefTo(current_method,
                                                      self.classes[class_info],
                                                      method_item, off)
                                        self.classes[class_info].AddMXrefFrom(
                                            method_item,
                                            self.classes[current_class.get_name()],
                                            current_method, off)

                                        # Internal xref related to class manipulation
                                        if class_info in instances_class_name and class_info != current_class.get_name(
                                        ):
                                            self.classes[current_class.get_name(
                                            )].AddXrefTo(REF_CLASS_USAGE,
                                                         self.classes[class_info],
                                                         method_item, off)
                                            self.classes[class_info].AddXrefFrom(
                                                REF_CLASS_USAGE,
                                                self.classes[current_class.get_name()],
                                                current_method, off)

                            # const-string/jumbo vAA, string@BBBB
                            elif 0x1a <= op_value <= 0x1b:
                                string_value = vm.get_cm_string(
                                    instruction.get_ref_kind())
                                if string_value not in self.strings:
                                    self.strings[string_value] = StringAnalysis(
                                        string_value)
                                self.strings[string_value].AddXrefFrom(
                                    self.classes[current_class.get_name()],
                                    current_method)

                            # sget, iget, sput, iput
                            elif 0x52 <= op_value <= 0x6d:
                                idx_field = instruction.get_ref_kind()
                                field_info = vm.get_cm_field(idx_field)
                                field_item = vm.get_field_descriptor(
                                    field_info[0], field_info[2], field_info[1])
                                if field_item:
                                    # read access to a field
                                    if (0x52 <= op_value <= 0x58) or (
                                            0x60 <= op_value <= 0x66):
                                        self.classes[current_class.get_name(
                                        )].AddFXrefRead(
                                            current_method,
                                            self.classes[current_class.get_name()],
                                            field_item)
                                    # write access to a field
                                    else:
                                        self.classes[current_class.get_name(
                                        )].AddFXrefWrite(
                                            current_method,
                                            self.classes[current_class.get_name()],
                                            field_item)

                            off += instruction.get_length()
                    except dvm.InvalidInstruction as e:
                        warning("Invalid instruction %s" % str(e))

    def get_method_novm(self, method):
        for vm in self.vms:
            if method in vm.get_methods():
                return MethodAnalysis(vm, method)
        return None

    @staticmethod
    def get_method(vm, method):
        return MethodAnalysis(vm, method)

    def get_method_by_name(self, class_name, method_name, method_descriptor):
        if class_name in self.classes:
            for method in self.classes[class_name].get_vm_class().get_methods():
                if method.get_name() == method_name and method.get_descriptor() == method_descriptor:
                    return method
        return None

    def get_method_analysis(self, method):
        class_analysis = self.get_class_analysis(method.get_class_name())
        if class_analysis:
            return class_analysis.get_method_analysis(method)
        return None

    def get_method_analysis_by_name(self, class_name, method_name, method_descriptor):
        method = self.get_method_by_name(class_name, method_name, method_descriptor)
        if method:
            return self.get_method_analysis(method)
        return None

    def get_field_analysis(self, field):
        class_analysis = self.get_class_analysis(field.get_class_name())
        if class_analysis:
            return class_analysis.get_field_analysis(field)
        return None

    def is_class_present(self, class_name):
        return class_name in self.classes

    def get_class_analysis(self, class_name):
        return self.classes.get(class_name)

    def get_strings_analysis(self):
        return self.strings

    def add(self, vm):
        self.vms.append(vm)

        for current_class in vm.get_classes():
            if current_class.get_name() not in self.classes:
                self.classes[current_class.get_name()] = ClassAnalysis(current_class)

    def get_vms(self):
        return self.vms

    def construct_class_hierarchy(self):
        for vm in self.vms:
            for current_class in vm.get_classes():
                parent_class = vm.get_class(current_class.sname)
                if parent_class:
                    parent_class.set_childs_class_name(current_class.name)
                else:
                    if current_class.sname in self.framework_hierarchy_childs.keys():
                        self.framework_hierarchy_childs[current_class.sname].append(current_class.name)
                    else:
                        self.framework_hierarchy_childs[current_class.sname] = []
                parent_interfaces = current_class.interfaces
                if parent_interfaces:
                    for pi in parent_interfaces:
                        if pi in self.framework_hierarchy_childs.keys():
                            self.framework_hierarchy_childs[pi].append(current_class.name)
                        else:
                            self.framework_hierarchy_childs[pi] = []

    def test_hierarchy(self):
        for vm in self.vms:
            for current_class in vm.get_classes():
                tmp_current = current_class
                if self.framework_class(tmp_current.name):
                    continue
                print tmp_current.name,
                while tmp_current and not self.framework_class(tmp_current.name) :
                    print '->' + tmp_current.sname,
                    if tmp_current.interfaces:
                        for interface in tmp_current.interfaces:
                            print '->' + interface,
                    tmp_current = vm.get_class(tmp_current.sname)



def is_ascii_obfuscation(vm):
    for classe in vm.get_classes():
        if is_ascii_problem(classe.get_name()):
            return True
        for method in classe.get_methods():
            if is_ascii_problem(method.get_name()):
                return True
    return False


class_hierarchy_framework = {}

class Test:
    def __init__(self):
        self.count = 0

    def parse_file_in_directory(self):
        org = [input_directory]
        while org:
            dst = []
            for diretory in org:
                for root, dirs, files in os.walk(diretory):
                    for fi in files:
                        if fi and fi.endswith(".java"):
                            with open(root + os.sep + fi, 'r') as rf:

                                for line in rf:
                                    if line.find("extends") != -1:
                                        if line.find("*") == -1:
                                            self.link_two(line)
                                            break
                    for di in dirs:
                        dst.append(di)
            org = dst

    @staticmethod
    def link_two(line):
        words = line.split(" ")
        source = ''
        dest = ''
        for key in xrange(len(words)):
            word = words[key]
            if word == 'extends':
                source = words[key-1]
                dest = words[key+1]
                break
        # print source
        # print dest
        if source != '' and dest != '':
            source_class = ''
            dest_class = ''
            for key in class_hierarchy_framework.keys():
                if key.find('/' + source + '.java') != -1:
                    source_class = key
                if key.find('/' + dest + '.java') != -1:
                    dest_class = key
            # print source_class
            # print dest_class
            if source_class != '' and dest_class != '':
                if 'parents' not in class_hierarchy_framework[source_class].keys():
                    class_hierarchy_framework[source_class]['parents'] = [dest_class]
                else:
                    class_hierarchy_framework[source_class]['parents'].append(dest_class)

                if 'childs' not in class_hierarchy_framework[dest_class].keys():
                    class_hierarchy_framework[dest_class]['childs'] = [source_class]
                else:
                    class_hierarchy_framework[dest_class]['childs'].append(source_class)
        else:
            # print 'do not get the source and dest'
            pass

    @staticmethod
    def get_class():
        org = [input_directory]
        while org:
            dst = []
            for directory in org:
                for root, dirs, files in os.walk(directory):
                    for fi in files:
                        if fi and fi.endswith(".java"):
                            pwd = root + os.sep + fi
                            idx = pwd.find("class_hierarchy")
                            cl = 'L' + pwd[idx + 16:]
                            class_hierarchy_framework[cl] = {}
                    for di in dirs:
                        dst.append(di)
            org = dst

input_directory = "/Users/wjk/Documents/class_hierarchy/"

