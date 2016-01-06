#
# with open("/Users/wjk/Desktop/flowdroidcg.txt", 'w') as wf:
#     with open('/Users/wjk/Desktop/output2.txt', 'r') as rf:
#         lines = rf.readlines()
#         lines.sort()
#         for line in lines:
#             wf.write(line)
import sys
if __name__ == '__main__':
    times = 0
    with open('/Users/wjk/Downloads/ImplicitEdges/ImplicitEdges2.txt', 'r') as rf:
        for line in rf:
            if line.find("setOnClickListener") != -1 and line.find("Landroid/view/View$OnClickListener") != -1 and line.find("onClick") != -1:
                times += 1
                print line
                # if times % 1000 == 13:
                #     print line

    print times

