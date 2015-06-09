#!/usr/bin/env python
# -*- coding: utf-8 -*-

from androguard.core.analysis import analysis

# get risk information about APK, for Huang xinyi
class Risk(object):

    @staticmethod
    def get_risk_evaluation(a, vm):     # APK and VmAnalysis
        risk = a.get_system_actions()
        permissions = a.get_system_permission()
        load_library = analysis.is_dyn_code(vm)

        with open(a.package + ".txt", 'w') as f:
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

