# buff = "digraph CFG {\n"
# for i in xrange(10000):
#     buff += str(i) + '\n'
#
# for i in xrange(9997):
#     buff += str(i) + ' -> ' + str(i+2) + '\n'
#
# buff += "}"

buff = ''
with open('graphviz.txt', 'r') as f:
    for line in f.readlines():
        str = ''
        for chra in line:
            if chra == '/':
                str += 'M'
            elif chra == '(' or chra == ')':
                str += 'F'
            elif chra == '$':
                str += 'IN'
            elif chra == '@':
                str += 'AT'
            elif chra == ';':
                str += 'END'
            else:
                str += chra
        buff += str


with open('changed.txt', 'w') as f:
    f.write(buff)

