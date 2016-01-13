#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from optparse import OptionParser
from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
from cfg import graphAnalysis
from androguard.core import androconf
from time import clock

option_0 = {'name': ('-i', '--input'), 'help': 'filename input (dex, apk)', 'nargs': 1}
options_io = [option_0]

registration_callback = {}


def get_registration_callback():
    with open('cfg/framework/ImplicitEdges.txt', 'r') as rf:
        for line in rf:
            reg, callback, pos = line.split('#')
            if reg not in registration_callback.keys():
                registration_callback[reg] = {}
            registration_callback[reg][pos] = callback


def one_apk_file_analysis(base_path):
    if not base_path:
        useage()
    start = clock()
    a = apk.APK(base_path)
    if a.is_valid_apk():
        vmx = None
        # multi-dex support
        for dex in a.get_all_dex():
            vm = dvm.DalvikVMFormat(dex)
            if vmx is None:
                vmx = analysis.NewVmAnalysis(vm)
            else:
                vmx.add(vm)
        if vmx is not None:
            vmx.construct_class_hierarchy()
            vmx.intro_procedural_cfg()
            vmx.explicit_icfg()
            vmx.implicit_icfg(registration_callback)
            with open('graphviz.dot', 'w') as f:
                f.write(vmx.export_to_dot())
        end = clock()
        print 'Analyzing the file ' + base_path + ' cost : ' + str(end-start) + "s"
    else:
        print 'the file ' + base_path + ' is a invalid apk file'


def many_apk_file_analysis(base_dir):
    if not base_dir:
        useage()
    for root, dirs, files in os.walk(base_dir):
        for dr in dirs:
            for r, d, fs in os.walk(base_dir + os.sep + dr):
                for f in fs:
                    if f.endswith(".apk"):
                        current_apk_file = base_dir + os.sep + dr + os.sep + f
                        one_apk_file_analysis(current_apk_file)


def useage():
    use = ''
    use += 'use this script to generate the cfg of the corresponding apk file\n'
    use += "type python 'cfg.py -i directory/to/apks' if you want analysis lots of apk\n"
    use += "type python 'cfg.py -i path/to/file.apk' if you want analysis just one apk file\n"
    use += 'have fun! If you have any question, mail to jkwangbest@gmail.com\n'
    exit(use)

if __name__ == '__main__':
    parser = OptionParser()
    time_begin = clock()
    for option in options_io:
        param = option['name']
        del option['name']
        parser.add_option(*param, **option)

    (option_input_output, _) = parser.parse_args()
    # get_registration_callback()

    # change if you want to analysis one apk or lots of apks
    # many_apk_file_analysis(option_input_output.input)
    one_apk_file_analysis(option_input_output.input)
    time_end = clock()
    print 'all the time cost is : ' + str(time_end-time_begin) + 's'

