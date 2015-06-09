#!/usr/bin/env python
# -*- coding: utf-8 -*-

# get risk information about APK, for Huang xinyi
class Risk(object):

    @staticmethod
    def get_risk_evaluation(a):
        risk = a.get_system_actions()
        permissions = a.get_system_permission()

        with open(a.package + ".txt", 'w') as file:
            file.write("ACTION"+'\n')
            for action in risk:
                file.write(action + '\n')
            file.write("PERMISSION" + '\n')
            for permission in permissions:
                file.write(permission+"\n")