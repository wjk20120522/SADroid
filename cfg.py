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

            # multi-dex support
            for dex in a.get_all_dex():
                vm = dvm.DalvikVMFormat(dex)
                if i == 0:
                    i += 1
                    vmx = analysis.NewVmAnalysis(vm)
                else:
                    vmx.add(vm)
            if vmx is not None:
                vmx.create_xref()
                with open('graphviz.txt', 'w') as f:
                    f.write(vmx.export_to_dot())
                # g = graphAnalysis.CFGAnalysis(vmx, a)   # generate CF
                # g.export_to_dot()

        else:
            print 'INVALID APK'


if __name__ == '__main__':
    from time import clock
    start = clock()
    parser = OptionParser()
    for option in options_io:
        param = option['name']
        del option['name']
        parser.add_option(*param, **option)

    (option_input_output, _) = parser.parse_args()
    main(option_input_output)
    end = clock()
    print 'Analyzing one apk time consumes : ' + str(end-start) + "s"

