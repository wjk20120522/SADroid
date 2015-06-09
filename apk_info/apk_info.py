#!/usr/bin/env python
# -*- coding:utf-8 -*-

class ApkInfo(object):

    @staticmethod
    def get_info(apk):
        info = apk.get_information_about_apk()
        # get information about APK, for Chen zhichao
        with open(apk.package + '.xml', 'w') as f:
            f.write(info)
