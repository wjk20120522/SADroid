import os
import sys

sys.path.append('../')
from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
from cfg import graphAnalysis
from time import clock


if __name__ == '__main__':
    for root, dirs, files in os.walk('../input'):
        for current_apk_file in files:
            cwd = os.path.abspath("../input")
            current_apk_file = cwd + os.sep + current_apk_file
            with open('blocks_nums.txt', 'a') as f:

                if current_apk_file.endswith(".apk"):
                    start = clock()
                    print 'Current Apk file name is: ' + current_apk_file
                    a = apk.APK(current_apk_file)
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
                            g = graphAnalysis.CFGAnalysis(vmx, a)   # generate CFG
                            end = clock()
                            print current_apk_file + " consumes : " + str(end-start) + "s"
                            f.write(current_apk_file + " consumes : " + str(end-start) + "s " +
                                    "blocks numbers is : " + str(g.blocks))
                else:
                    print 'INVALID APK'

