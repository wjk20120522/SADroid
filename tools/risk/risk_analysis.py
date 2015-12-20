#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from optparse import OptionParser

from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
from cfg import graphAnalysis
from androguard.core import androconf



option_0 = {'name': ('-i', '--input'), 'help': 'filename input (dex, apk)', 'nargs': 1}

options_io = [option_0]

risk_permissions = {
    'android.permission.CALL_PHONE': 5,
    'android.permission.INSTALL_PACKAGES': 4,
    'android.permission.INTERNET': 2,
    'android.permission.PROCESS_OUTGOING_CALLS': 4,
    'android.permission.READ_CONTACTS': 3,
    'android.permission.READ_PHONE_STATE': 3,
    'android.permission.READ_SMS': 4,
    'android.permission.RECEIVE_MMS': 2,
    'android.permission.RECEIVE_SMS': 4
}

risk_APIs = {
    'abortBroadcast': 1,
    'getDeviceId': 5,
    'getInstalledPackages': 3,
    'getSimSerialNumber': 5,
    'getSimState': 5,
    'getSubscriberId': 5,
    'sendTextMessage': 5
}


def main(options):
    if options.input is not None:
        a = apk.APK(options.input)
        risk_permission_value = 0.0
        risk_apis = 0.0
        permissions = a.get_no_duplicate_permission()
        for permission in permissions:
            if permission in risk_permissions.keys():
                risk_permission_value += risk_permissions[permission]

        risk_permission_value /= 8

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
                apis = create_xref(vmx)
                for api in apis:
                    risk_apis += api
                risk_apis /= 7

        else:
            print 'INVALID APK'

        print 'the risk of apk is : %f', (risk_permission_value + risk_apis) / 2


def create_xref(self):
        for last_vm in self.vms:
            for current_class in last_vm.get_classes():
                for current_method in current_class.get_methods():
                    code = current_method.get_code()
                    if code is None:
                        continue

                    off = 0
                    bc = code.get_bc()
                    try:
                        for instruction in bc.get_instructions():
                            op_value = instruction.get_op_value()

                            # invoke-kind /range {vC, vD, vE, vF, vG}, meth@BBBB
                            if (0x6e <= op_value <= 0x72) or (0x74 <= op_value <= 0x78):
                                idx_meth = instruction.get_ref_kind()
                                method_info = last_vm.get_cm_method(idx_meth)
                                if method_info:
                                    if method_info[1] in risk_APIs.keys():
                                        yield risk_APIs[method_info[1]]

                            off += instruction.get_length()
                    except dvm.InvalidInstruction as e:
                        warning("Invalid instruction %s" % str(e))


if __name__ == '__main__':
    parser = OptionParser()
    for option in options_io:
        param = option['name']
        del option['name']
        parser.add_option(*param, **option)

    (option_input_output, _) = parser.parse_args()
    main(option_input_output)
