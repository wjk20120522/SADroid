#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.pardir)

from androguard.core.bytecodes import apk
from optparse import OptionParser


option_0 = {'name': ('-i', '--input'), 'help': 'directory of apk', 'nargs': 1}
option_1 = {'name': ('-o', '--output'), 'help': 'directory of output', 'nargs': 1}

options_io = [option_0, option_1]


def get_risk_evaluation(a, output, count):      # APK and VmAnalysis
        risk = a.get_system_actions()
        permissions = a.get_system_permission()

        with open(output + str(count) + ".txt", 'w') as f:
            f.write("ACTION"+'\n')
            for action in risk:
                f.write(action + '\n')
            f.write("PERMISSION" + '\n')
            for permission in permissions:
                f.write(permission+"\n")
            # if load_library:
            #     f.write("Loadlibrary:True" + '\n')
            # else:
            #     f.write("Loadlibrary:False" + '\n')


def main(input_output):
    # if input_output.input is not None and input_output.output is not None:
    path = input_output.input

    count = 1
    for root, dirs, files in os.walk(path):

        for f in files:

            print 'begin analysis the ' + str(count) + " file " + f
            print '........................'
            a = apk.APK(root + os.sep + f)

            if a.is_valid_APK():
                # vm = dvm.DalvikVMFormat(a.get_dex())
                # vmx = analysis.VMAnalysis(vm)
                get_risk_evaluation(a, input_output.output, count)
                print 'end analysis the ' + str(count) + " file"
                count += 1

if __name__ == "__main__":

    parser = OptionParser()
    for option in options_io:
        param = option['name']
        del option['name']
        parser.add_option(*param, **option)

    (option_input_output, _) = parser.parse_args()
    main(option_input_output)
