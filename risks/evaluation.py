#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wjk/Desktop/SADroid/")

from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
from optparse import OptionParser
import os


option_0 = {'name': ('-i', '--input'), 'help': 'directory of apk', 'nargs': 1}
option_1 = {'name': ('-o', '--output'), 'help': 'directory of output', 'nargs': 1}

options_io = [option_0, option_1]

def get_risk_evaluation(a, vm, output):     # APK and VmAnalysis
        risk = a.get_system_actions()
        permissions = a.get_system_permission()
        load_library = analysis.is_dyn_code(vm)

        with open(output + a.package + ".txt", 'w') as f:
            f.write("ACTION"+'\n')
            for action in risk:
                f.write(action + '\n')
            f.write("PERMISSION" + '\n')
            for permission in permissions:
                f.write(permission+"\n")
            if load_library:
                f.write("Loadlibrary:True" + '\n')
            else:
                f.write("Loadlibrary:False" + '\n')


def main(input_output):
    # if input_output.input is not None and input_output.output is not None:
    path = input_output.input

    for root, dirs, files in os.walk(path):

        for f in files:
            print f + "-------"
            a = apk.APK(path + f)

            if a.is_valid_APK():
                vm = dvm.DalvikVMFormat(a.get_dex())
                vmx = analysis.VMAnalysis(vm)
                get_risk_evaluation(a, vmx, input_output.output)


if __name__ == "__main__":

    parser = OptionParser()
    for option in options_io:
        param = option['name']
        del option['name']
        parser.add_option(*param, **option)

    (option_input_output, _) = parser.parse_args()
    main(option_input_output)