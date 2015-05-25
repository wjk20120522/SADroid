#!/usr/bin/python

# gain the instructions of each methods,

import re

from androguard.core.bytecodes import apk, dvm  # api_permissions,api_permissions_AfterChange
from permissions import CompleteAPIMap_Andro

PERM_MAP = CompleteAPIMap_Andro.PERMISSIONS  # completeAPIMap_ALL.PERMISSIONS
ALLPERMISSIONS = PERM_MAP.keys()    # 169 items

with open('permissions/dynamicIntentPerm', 'r') as f:
    dynamic_recordstr = f.read()

dynamic_record_list = dynamic_recordstr.split('\n')


INTENT_FUNC_PROTECTED = ['startActivity(Landroid/content/Intent;)',
           'startActivityForResult(Landroid/content/Intent;)',
           'startService(Landroid/content/Intent;)',
           'registerReceiver(Landroid/content/BroadcastReceiver; Landroid/content/IntentFilter;)'
]

INTENT_FUNC_ALL = ['startActivity(Landroid/content/Intent;',
           'startActivityForResult(Landroid/content/Intent;',
           'startService(Landroid/content/Intent;',
           'sendBroadcast(Landroid/content/Intent;',
           'sendOrderedBroadcast(Landroid/content/Intent;',
           'sendBroadcastAsUser(Landroid/content/Intent;',
           'sendOrderedBroadcastAsUser(Landroid/content/Intent;',
           'getBroadcast(Landroid/content/Context; I Landroid/content/Intent;',
           'getService(Landroid/content/Context; I Landroid/content/Intent;',
           'registerReceiver(Landroid/content/BroadcastReceiver; Landroid/content/IntentFilter;',
           'init(Ljava/lang/String;'
]

# search undirect call of intents, such as intent.CALL
def intent_search_startActivity(targetCodeArray): # success

    intent_top = ''
    action = ''
    uri = ''
    action_variable = ''
    uri_variable = ''
    action_or_uri_variable = []

    for i in range(len(targetCodeArray))[::-1]:
        if intent_top == '':
            t_startAc = re.findall('invoke.*? (.*), L.*startActivity', targetCodeArray[i])
            if t_startAc:
                argus_list = t_startAc[0].split(', ')
                try:
                    intent_top = argus_list[1]
                except IndexError:
                    print 'Error'
            else:
                continue
        else:
            if action_or_uri_variable == [] or action_variable =='' or uri_variable == '':
                t_actionoruri = re.findall('invoke.*%s,(.*), Landroid/content/Intent.*init.*?(.*);\)'% intent_top, targetCodeArray[i])
                if t_actionoruri:
                    action_or_uri_tmp = t_actionoruri[0][0].split(',')
                    action_or_uri_variable =  action_or_uri_tmp

                    if len(action_or_uri_variable) ==1:
                        action_or_uri =  re.sub(' ','', action_or_uri_tmp[0])
                        if re.findall('Ljava/lang/String',t_actionoruri[0][1]):
                            action_variable = action_or_uri
                            continue
                        if re.findall('Landroid/net/Uri',t_actionoruri[0][1]):
                            uri_variable = action_or_uri
                            continue
                    else:# two paras
                        idetify_info = t_actionoruri[0][1].split(';')
                        if re.findall('Ljava/lang/String',idetify_info[0]):
                            action_variable = re.sub(' ','', action_or_uri_tmp[0])

                            uri_variable = re.sub(' ','', action_or_uri_tmp[1])
                            continue
                        else:
                            uri_variable = re.sub(' ','', action_or_uri_tmp[0])
                            action_variable = re.sub(' ','', action_or_uri_tmp[1])
                            continue

                else:
                    continue # not sure
            if action_or_uri_variable!=[]:
                if action == '' or uri == '':
                    t_action_or_uri = re.findall("const-string %s, \'(.*)\'"% action_variable, targetCodeArray[i])
                    if t_action_or_uri:
                        try:

                            action = t_action_or_uri[0]
                            continue
                        except IndexError:
                            pass
                    else:
                        t_action_or_uri = re.findall("const-string %s, \'(.*)\'"% uri_variable, targetCodeArray[i])
                        if t_action_or_uri:
                            try:
                                uri = t_action_or_uri[0]
                            except IndexError:
                                pass
                        else:
                            continue

                else:
                    continue
            else:
                continue

    return action + ';' + uri


def intent_search_startService(TargetcodeArray):

    intent_name = ''
    action_name = ''
    action_list = []

    for i in range(len(TargetcodeArray))[::-1]:
        if not intent_name:
            tmp = re.findall('invoke.*\d, (.*), L.*startService', TargetcodeArray[-1])
            if tmp:
                intent_name = tmp[0]
            else:
                pass
        else:
            tmp1 = re.search("invoke.*%s,.*Landroid/content/Intent;-><init>"% intent_name,TargetcodeArray[i])
            if tmp1:
                break

            tmp2 = re.findall('invoke.*%s, (.*), Landroid/content/Intent;->setAction'% intent_name, TargetcodeArray[i])
            if tmp2:
                action_name = tmp2[0]
                continue
            tmp3 = re.findall("const-string %s, '(.*)'"% action_name, TargetcodeArray[i])
            if tmp3:
                action_list.append(tmp3[0])
    print action_list
    return action_list


def intent_search_receiver(TargetcodeArray, call_func, func_argus):

    action_list = []

    #handle different funcs
    argus_type_array  = func_argus.split(';')
    for i in range(len(argus_type_array)-1):
        if re.search('Landroid/content/IntentFilter',argus_type_array[i]):
            break
        else:
            continue
    argus_name_str = re.findall('invoke.*? (.*), L.*%s'% call_func, TargetcodeArray[-1])
    if re.search('\.\.\.',argus_name_str[0]): #argusments list
        tmp = re.findall('v(\d) ... v(\d)', argus_name_str[0])
        if tmp:
            filter_argus_name = 'v' + '%s'% (int(tmp[0][0])+ i + 1)
        else:
            filter_argus_name = 'v1'
    else:
        argus_name_array = argus_name_str[0].split(', ')
        filter_argus_name = argus_name_array[i+1]

    print filter_argus_name
    action_name = ''
    singleaction = False

    for i in range(len(TargetcodeArray))[::-1]:
        tmp = re.search("invoke.*%s,.*Landroid/content/IntentFilter;-><init>"% filter_argus_name,TargetcodeArray[i])
        if tmp:
            tmp = re.findall("invoke.*%s, (.*), Landroid/content/IntentFilter;-><init>"% filter_argus_name,TargetcodeArray[i])
            if not tmp:
                break
            else:
                singleaction = True
                action_name = tmp[0]
                continue
        if singleaction:
            tmp3 = re.findall("const-string %s, \'(.*)\'"% action_name,TargetcodeArray[i])
            if tmp3:
                action_list.append(tmp3[0])
                break

        tmp2 = re.findall("invoke.*%s, (.*), Landroid/content/IntentFilter;->addAction"% filter_argus_name, TargetcodeArray[i])
        if tmp2 and (not action_name):
            action_name = tmp2[0]
            continue
        if action_name:
            tmp3 = re.findall("const-string %s, \'(.*)\'"% action_name,TargetcodeArray[i])
            action_name = ''
            if tmp3:
                action_list.append(tmp3[0])
            else:
                continue


    return action_list

# search CP
def cp_search(targetCodeArray): # success
    urivariable = ''
    uri_calltype = ''
    uri = ''

    for i in range(len(targetCodeArray))[::-1]:
        if urivariable == '': # ContentResolver is short for CR
            t_callCR = re.findall('invoke.*? (.*), L.*->(.*)\(', targetCodeArray[i]) # find variable, format depend on func(query or insert/unpdate/delete)
            if t_callCR:
                if t_callCR[0][1]=='query': # 5 arguments
                    urivariable_tmp = re.findall('v(\d) ...', t_callCR[0][0])
                    if urivariable_tmp:
                        try:
                            urivariable = 'v' + '%s'% (int(urivariable_tmp[0])+1)
                        except IndexError:
                            pass
                    else:
                        try:
                            urivariable = t_callCR[0][0].split(', ')[1]
                        except IndexError:
                            pass

                else: # insert/update/delete , the first argus is URI Object
                    urivariable_tmp=re.findall('v(\d) ...', t_callCR[0][0])
                    if urivariable_tmp:
                        try:
                            urivariable = 'v' + '%s'% (int(urivariable_tmp[0])+1)
                        except IndexError:
                            pass
                    else:
                        print t_callCR

                        try:
                            urivariable = t_callCR[0][0].split(', ')[1]
                        except IndexError:
                            print t_callCR
            else:
                continue
        else:
            if uri_calltype=='' and urivariable:
                t_calluritype = re.search('invoke.* %s, Landroid/net/Uri;->parse'% urivariable, targetCodeArray[i])
                if t_calluritype:
                    uri_calltype = 'const-string'
                else:
                    t_parse_call = re.search('move-result-object %s'% urivariable, targetCodeArray[i])
                    if t_parse_call:
                        continue
                    else:
                        uri_calltype = 'sget-object'

            else:
                if uri=='' and uri_calltype:
                    if uri_calltype=='const-string':
                        contenturi_tmp = re.findall('%s %s, \'(.*)\''%(uri_calltype,urivariable), targetCodeArray[i])
                        try:
                            uri = contenturi_tmp[0]
                        except IndexError:
                            continue
                    else:
                        if uri_calltype=='sget-object':
                            contenturi_tmp = re.findall('%s %s, (L.*) Landroid/net/Uri'%(uri_calltype,urivariable), targetCodeArray[i])
                            try:
                                uri = contenturi_tmp[0]
                            except IndexError:
                                continue
                        else:
                            continue

                else:
                    continue
    return uri

def cp_uri_search(targetCodeArray, setdataindex):

    Is_used = False
    uri_type = ''
    uri = ''
    intent_uri_tmp = re.findall("invoke.*? (.*), Landroid/content/Intent;->setData", targetCodeArray[setdataindex])
    if intent_uri_tmp:
        intent_uri = intent_uri_tmp[0].split(', ')
        intent_name = intent_uri[0]
        uri_name = intent_uri[1]

    for i in range(setdataindex,len(targetCodeArray))[::-1]:
        opera_tmp = re.findall("invoke.*?%s.*?->(.*)\("% intent_name, targetCodeArray[i])
        if opera_tmp:
            if is_INTENT_opera_name(opera_tmp[0]):
                Is_used = True
                break

    if Is_used:
        for i in range(0,setdataindex)[::-1]:
            if uri_type=='' and uri_name:
                uritype_tmp = re.search('invoke.* %s, Landroid/net/Uri;->parse'% uri_name, targetCodeArray[i])
                if uritype_tmp:
                    uri_type = 'const-string'
                else:
                    uritype_another_tmp = re.search('move-result-object %s'% uri_name, targetCodeArray[i])
                    if uritype_another_tmp:
                        continue
                    else:
                        uri_type = 'sget-object'

            else:
                if uri=='' and uri_type:
                    if uri_type=='const-string':
                        contenturi_tmp = re.findall('%s %s, \'(.*)\''%(uri_type,uri_name), targetCodeArray[i])
                        try:
                            uri = contenturi_tmp[0]
                        except IndexError:
                            continue
                    else:
                        if uri_type=='sget-object':
                            contenturi_tmp = re.findall('%s %s, (L.*) Landroid/net/Uri'%(uri_type,uri_name), targetCodeArray[i])
                            try:
                                uri = contenturi_tmp[0]
                            except IndexError:
                                continue
                        else:
                            continue

                else:
                    continue
    return uri

# verify whether func which has a package named "Landroid/content/ContentResolver" execute RW operation
def is_CP_opera(func):
    opera_list = ['query','getType','insert','update','delete']
    for opera in opera_list:
        if func==opera:
            return True
        else:
            continue
    return False

def is_intent_opera(func, arguments):
    for opera in INTENT_FUNC_PROTECTED:
        tmp = re.findall('(.*)\((.*)\)', opera)
        if tmp:
            if func == tmp[0][0] and re.search(tmp[0][1], arguments):
                print func, arguments
                return True
        else:
            continue
    return False

# add for setData
def is_INTENT_opera_name(func):
    for opera in INTENT_FUNC_ALL:
        tmp = re.findall('(.*)\(', opera)
        if tmp:
            if re.search(tmp[0],func):
                return True
        else:
            continue
    return False

# Search Permission in MAPDict accord target package and fuc
def Search_func(MAPDict, Package, Func, IntentORCP, argus, Class_name, Method_name, SameMethod_mark,PermUseMap):
    for perm in MAPDict:
        for pack in MAPDict[perm]:
            if pack == Package:
                Pack_list = MAPDict[perm][pack]
                mark = 'helo'
                if IntentORCP == 'intent': # success
                    for i in range (0,len(Pack_list)):
                        if Pack_list[i][1] == Func and re.match(Pack_list[i][2],argus):
                            if mark != Func + argus: # Same call process once
                                UseDetail = Class_name +' '+ Method_name + '() ---> ' + pack + '->' + Func + '('+ argus + ')\n'
                                try:
                                    origil = PermUseMap[perm]
                                    PermUseMap[perm] = origil + UseDetail
                                except KeyError:
                                    PermUseMap[perm] = UseDetail

                                mark = Pack_list[i][1] + Pack_list[i][2]
                                SameMethod_mark=1


                            else:
                                continue
                        else:
                            continue
                else:
                    if IntentORCP == 'cp':
                        for i in range (0,len(Pack_list)):
                            if Pack_list[i][1] == Func and Pack_list[i][2]==argus: # MATCH means Containing
                                if mark != Func + argus: # Same call process once
                                    UseDetail = Class_name +' '+ Method_name + '() ---> ' + pack + '->' + Func + '(URI:' + argus+')\n'
                                    try:
                                        origil = PermUseMap[perm]
                                        PermUseMap[perm] = origil + UseDetail
                                    except KeyError:
                                        PermUseMap[perm] = UseDetail

                                    mark = Pack_list[i][1] + Pack_list[i][2]
                                    SameMethod_mark=1



                                else:
                                    continue
                            else:
                                continue

                    else:

                        # Normal Function
                        for i in range (0,len(Pack_list)):
                            if Pack_list[i][1] == Func: # Normal func, just match func_name
                                if mark != Func + argus: # Same call process once
                                    UseDetail = Class_name +' '+ Method_name + '() ---> ' + pack + '->' + Func + '() '+ Pack_list[i][2]+'\n'
                                    try:
                                        origil = PermUseMap[perm]
                                        PermUseMap[perm] = origil + UseDetail
                                    except KeyError:
                                        PermUseMap[perm] = UseDetail

                                    mark = Pack_list[i][1] + Pack_list[i][2]
                                    SameMethod_mark=1

                                    return SameMethod_mark

                                else:
                                    continue
                            else:
                                continue

            else:
                continue
    return SameMethod_mark


def search_receiver_perm(actionlist,packagename,callfunc,classname,methodname,permuseMap):
    for record in dynamic_record_list:
        for action in actionlist:
            if re.search(action,record):
                perm_tmp =  re.findall('  (.*)',record)
                perm = perm_tmp[0]
                UseDetail = classname +' '+ methodname + '() ---> ' + packagename + '->'     + callfunc + '(Intent:'+ action +')\n'
                try:
                    origil = permuseMap[perm]
                    permuseMap[perm] = origil + UseDetail
                except KeyError:
                    permuseMap[perm ] = UseDetail
            else:
                continue

# Scan all Dcode, for setData searching
def chan_allinstruc_to_StrArray(bc):
    instruc_str_array = []
    idx = 0
    for i in bc.get_instructions():
        temp = "%x" % idx+' '+i.get_name() +' '+ i.get_output()
        instruc_str_array.append(temp)
        idx += i.get_length()
    return instruc_str_array

#   Scan Dcode, put all the instructions in a String Array
def chan_instruc_to_StrArray(bc,index):
    instruc_str_array = []
    idx = 0
    count = 0
    for i in bc.get_instructions():
        if count<=index:
            temp = "%x" % idx+' '+i.get_name() +' '+ i.get_output()
            instruc_str_array.append(temp)
            idx += i.get_length()
            count += 1
        else:
            break

    return instruc_str_array


# Gain the func in APK, call the Search func to FIND used PERM 
def search_permission_api(apkfile):

    a = apk.APK(apkfile)
    # a.get_permissions()
    d = dvm.DalvikVMFormat(a.get_dex())

    # dx = analysis.VMAnalysis(d)
    # analysis.show_Permissions(dx)

    PermUseMap = {}     #Build a PermUseTable

    for each_method in d.get_methods():

        class_name = each_method.get_class_name()
        method_name = each_method.get_name()
        SameMethod = 0

        #  Define the range of scan, become more quick
        if re.match('Landroid/support/v4', class_name) is None and re.match('Landroid/support/v7', class_name) is None:
            code = each_method.get_code()

            if code:
                bc = code.get_bc()
                instruc_count = 0

                for i in bc.get_instructions():
                    t2 = i.get_name()
                    pattern2 = re.compile('invoke')
                    match = pattern2.search(t2)

                    if match:
                        index = instruc_count
                        # Futhe,mple/test_callphone/MainActivity;abstract the Func within instruction
                        intent_or_cp = 'normal function'
                        instruc_target = i.get_output()

                        pattern3 = re.compile(u'(L.*)->(.*)(\(.*\))') # package,func,arguments
                        search_result = pattern3.findall(instruc_target)
                        if search_result:
                            package_name = search_result[0][0]
                            call_func = search_result[0][1]
                            func_argus = search_result[0][2]
                            # Intent
                            if is_intent_opera(call_func, func_argus):
                                code_str_array = chan_instruc_to_StrArray(bc, index)
                                if re.search('startActivity', call_func):
                                    # print "startactivity"
                                    action_uri_list = intent_search_startActivity(code_str_array).split(';')
                                    intent_or_cp = 'intent'
                                    package_name = re.sub('\((.*)\)','\g<1>',search_result[0][2]) # the argument of startActivity is intent
                                    call_func = action_uri_list[0] # when call ACTION
                                    func_argus = action_uri_list[1]

                                else:
                                    if re.search('startService',call_func):
                                        # print "startService",class_name,method_name
                                        action_list = intent_search_startService(code_str_array)
                                        package_name = re.sub('\((.*)\)','\g<1>',search_result[0][2]) # the argument of startService is intent
                                        intent_or_cp = 'intent'
                                        if len(action_list) == 1:
                                            if action_list[0]:
                                                call_func = action_list[0] # when call ACTION
                                                func_argus = 'null'
                                        else:
                                            for action in action_list:
                                                call_func = action
                                                func_argus = 'null'
                                                SameMethod_t = Search_func(PERM_MAP, package_name, call_func, intent_or_cp, func_argus, class_name, method_name, SameMethod, PermUseMap)
                                                SameMethod = SameMethod_t  # Mar
                                            instruc_count += 1
                                            continue

                                    else:
                                        # print package_name, method_name,call_func
                                        action_list = intent_search_receiver(code_str_array, call_func, func_argus)
                                        # print action_list
                                        method_name = each_method.get_name()
                                        search_receiver_perm(action_list,package_name,call_func,class_name,method_name,PermUseMap)
                                        instruc_count += 1
                                        continue

                            #cp
                            else:
                                if package_name== 'Landroid/content/ContentResolver;' and is_CP_opera(call_func):
                                    code_str_array = chan_instruc_to_StrArray(bc,index)
                                    content_uri = cp_search(code_str_array)
                                    intent_or_cp = 'cp'
                                    func_argus = content_uri
                                if package_name=='Landroid/content/Intent;' and (call_func=='setData'):
                                    code_str_array = chan_allinstruc_to_StrArray(bc)
                                    content_uri = cp_uri_search(code_str_array, index)
                                    intent_or_cp = 'cp'
                                    func_argus = content_uri
                            method_name = each_method.get_name()
                            SameMethod_t = Search_func(PERM_MAP, package_name, call_func, intent_or_cp, func_argus, class_name, method_name, SameMethod, PermUseMap)
                            SameMethod = SameMethod_t  # Mark whether these funcs are in the same METHOD

                    instruc_count += 1

    return PermUseMap

if __name__ == '__main__':
    PermUseMap = search_permission_api("apk/com.hcg.cok.gp.apk")
    for permission in PermUseMap.keys():
        print permission
    print len(PermUseMap.keys())
    print 'love'














