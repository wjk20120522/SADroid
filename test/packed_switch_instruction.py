import os
import sys

sys.path.append('../')
from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis

if __name__ == '__main__':
    for root, dirs, files in os.walk('../input'):
        for current_apk_file in files:
            cwd = os.path.abspath("../input")
            current_apk_file = cwd + os.sep + current_apk_file
            if current_apk_file.endswith(".apk"):
                print 'Current Apk file name is: ' + current_apk_file
                a = apk.APK(current_apk_file)
                if a.is_valid_apk():
                    vm = dvm.DalvikVMFormat(a.get_dex())
                    vmx = analysis.newVMAnalysis(vm)
                    vmx.explicit_icfg()
                else:
                    print 'Invalid Apk'
                    exit()

