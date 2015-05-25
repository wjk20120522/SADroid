#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from optparse import OptionParser
from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis, ganalysis
from androguard.core import androconf
from androguard.util import read

option_0 = {'name': ('-i', '--input'), 'help': 'filename input (dex, apk)', 'nargs': 1}
option_1 = {'name': ('-o', '--output'), 'help': 'filename output of the gexf', 'nargs': 1}

options_io = [option_0, option_1]

def main(options):
    if options.input is not None and options.output is not None:
        vm = None
        a = apk.APK(options.input)

        if a.is_valid_APK():
            vm = dvm.DalvikVMFormat(a.get_dex())
        else:
            print 'INVALID APK'
            exit()

        vmx = analysis.VMAnalysis(vm)
        gvmx = ganalysis.GVMAnalysis(vmx, a)

        b = gvmx.export_to_gexf()
        androconf.save_to_disk(b, options.output)
        # after all is done, test the time
        print 'After all job of a application is done, the time is'
        print time.strftime("%H:%M:%S", time.localtime())

if __name__ == '__main__':
    # just test the cost time of each application
    import time
    print 'begin time of App'
    print time.strftime("%H:%M:%S", time.localtime())
    parser = OptionParser()
    for option in options_io:
        param = option['name']
        del option['name']
        parser.add_option(*param, **option)

    (option_input_output, _) = parser.parse_args()
    main(option_input_output)