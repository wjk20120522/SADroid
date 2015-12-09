#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser

from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
from cfg import graphAnalysis
from androguard.core import androconf

option_0 = {'name': ('-i', '--input'), 'help': 'filename input (dex, apk)', 'nargs': 1}
option_1 = {'name': ('-o', '--output'), 'help': 'filename output of the gexf', 'nargs': 1}

options_io = [option_0, option_1]


def main(options):
    if options.input is not None:
        a = apk.APK(options.input)
        i = 0
        if a.is_valid_apk():
            vmx = None

            for dex in a.get_all_dex():
                vm = dvm.DalvikVMFormat(dex)
                if i == 0:
                    i += 1
                    vmx = analysis.NewVmAnalysis(vm)
                else:
                    vmx.add(vm)
                vmx.create_xref()

            # if vmx is not None:
            #     vmx.create_xref()
        else:
            print 'INVALID APK'
            exit()


if __name__ == '__main__':
    parser = OptionParser()
    for option in options_io:
        param = option['name']
        del option['name']
        parser.add_option(*param, **option)

    (option_input_output, _) = parser.parse_args()
    main(option_input_output)
