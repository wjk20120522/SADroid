import sys



exit()
'''
if __name__ == '__main__':
    with open('/Users/wjk/Downloads/ImplicitEdges/ImplicitEdges.txt', 'r') as rf:
        with open('/Users/wjk/Downloads/ImplicitEdges/ImplicitEdges2.txt', 'w') as wf:
            for line in rf:
                reg, callback, pos = line.split('#')
                reg = reg.split('.')
                len1 = len(reg)-1
                tmp = 'L'
                for key,r in enumerate(reg):
                    if key != 0:
                        if key == len1:
                            tmp += ';->'
                        else:
                            tmp += '/'
                    tmp += r
                tmp += '#'

                callback = callback.split('.')
                for key,r in enumerate(callback):
                    if key != 0:
                        if key == len1:
                            tmp += ';->'
                        else:
                            tmp += '/'
                    tmp += r
                tmp += '#'
                tmp += str(pos)

                wf.write( tmp )
'''

count = 0

if __name__ == '__main__':
    with open('/Users/wjk/Downloads/ImplicitEdges/ImplicitEdges3.txt', 'r') as rf:
            for line in rf:

                if line.find("Landroid/app/Instrumentation;->callActivity") != -1 \
                        and line.find("(Landroid/app/Activity;Landroid/os/Bundle;)") != -1\
                        and line.find("onResume") != -1:
                    count += 1
                    # print line
                # reg = reg.split(':')
                # reg = ''.join(reg)
                # callback = callback.split(':')
                # callback = ''.join(callback)
                #
                # wf.write( reg + '#' + callback + '#'  + str(pos))
            print count
