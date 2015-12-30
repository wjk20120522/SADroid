
l = []

if l is []:
    print 'l is []'

if not l:
    print 'l == []'

exit()


with open("/Users/wjk/Desktop/output2.txt", 'w') as wf:
    with open('/Users/wjk/Desktop/flowdroidcg.txt', 'r') as rf:
        lines = rf.readlines()
        lines.sort()
        for line in lines:
            wf.write(line)
