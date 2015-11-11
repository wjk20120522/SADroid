#!/usr/bin/env python
# -*- coding: utf-8 -*-

from androguard.core.bytecodes import apk, dvm
from optparse import OptionParser
from androguard.core.analysis import analysis
from cfg import graphAnalysis
from androguard.core import androconf
import time
import logging

class ApkInfo(object):

    @staticmethod
    def get_info(apk, output):
        info = apk.get_information_about_apk()
        output += time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + ".xml"
        with open(output, 'w') as f:
            f.write(info)


option_0 = {'name': ('-i', '--input'), 'help': 'filename input (dex, apk)', 'nargs': 1}
option_1 = {'name': ('-o', '--output'), 'help': 'filename output of the gexf', 'nargs': 1}

options_io = [option_0, option_1]

def main(options):
    if options.input is not None and options.output is not None:
        vm = None

        print options.input
        a = apk.APK(options.input)

        if a.is_valid_APK():
            vm = dvm.DalvikVMFormat(a.get_dex())
        else:
            print 'INVALID APK'
            exit()

        ApkInfo.get_info(a, options.output)


if __name__ == '__main__':
    # just test the cost time of each application
    import time

    parser = OptionParser()
    for option in options_io:
        param = option['name']
        del option['name']
        parser.add_option(*param, **option)

    (option_input_output, _) = parser.parse_args()
    main(option_input_output)


