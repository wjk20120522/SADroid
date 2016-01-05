import os
import sys

# 检查下载的APK是否有损坏

sys.path.append('../')
from androguard.core.bytecodes import apk, dvm

base_dir = '/Users/wjk/Desktop/apks'
if __name__ == '__main__':
    for root, dirs, files in os.walk(base_dir):
        for dr in dirs:
            for r, d, fs in os.walk(base_dir + os.sep + dr):
                for f in fs:
                    if f.endswith(".apk"):
                        current_apk_file = base_dir + os.sep + dr + os.sep + f
                        a = apk.APK(current_apk_file)
                        if a.is_valid_apk():
                            package_name = a.get_package() + ".apk"
                            if package_name != f:
                                print 'the file ' + current_apk_file + " is broken "
                        else:
                            print 'Invalid Apk'
                            exit()
