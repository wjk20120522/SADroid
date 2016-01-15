import sys

sys.path.append('../')


test = {}
test['12'] = []
test['23'] = []
for key in test.keys():
    if key == '12':
        print '12 is key'

exit()



with open('../cfg/framework/ImplicitEdges.txt', 'r') as rf:
        count = 0
        for line in rf:
            reg, click, num = line.split("#")
            if reg.find("Landroid/view/View;->setOnClickListener") != -1 and reg.find("Landroid/view/View$OnClickListener;") != -1\
                    and click.find("onClick") != -1:
                print line
                count += 1
        print count
exit()


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
