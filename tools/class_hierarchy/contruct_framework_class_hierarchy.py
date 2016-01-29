import os
import re
import os.path
import sys

class_hierarchy_framework = {}

parent_directory = 'class_hierarchy/'
input_directory = "/Users/wjk/Documents/class_hierarchy/"


class Node:

    def __init__(self, t='class', n=''):
        self.type = t
        self.name = n
        self.childs = []
        self.parents = []

    def add_child(self, child):
        self.childs.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def set_type(self, t):
        self.type = t

class Test:
    def __init__(self):
        self.count = 0

    def parse_file_in_directory(self):
        org = [input_directory]
        while org:
            dst = []
            for diretory in org:
                for root, dirs, files in os.walk(diretory):
                    for fi in files:
                        if fi and fi.endswith(".java"):
                            with open(root + os.sep + fi, 'r') as rf:
                                imports = Test.get_imports(root + os.sep + fi)
                                idx = root.find(parent_directory)
                                cp = 'L' + root[idx+len(parent_directory):] + os.sep
                                lines = rf.readlines()
                                for i in xrange(len(lines)):
                                    if Test.first_line_of_class(lines[i]):
                                        if lines[i].find('}') == -1:
                                            if lines[i].find("{") == -1:
                                                tmp = i+1
                                                while lines[tmp].find("{") == -1:
                                                    lines[i] += lines[tmp]
                                                    tmp += 1
                                                lines[i] += lines[tmp]
                                            self.get_three(lines[i], cp, imports, root)

                    for di in dirs:
                        dst.append(di)
            org = dst

    @staticmethod
    def get_imports(file_name):
        imports = []
        with open(file_name, 'r') as rf:
            for line in rf:
                if line.startswith("import"):
                    cl = line.split(' ')[-1]
                    cl = cl[:-2]    # discard ';\n'
                    imports.append('L' + '/'.join(cl.split(".")))
        return imports

    @staticmethod
    def first_line_of_class(line):
        if line.find("*") != -1:
            return False
        if line.find("class") == -1 and line.find("interface") == -1:
            return False
        if line.startswith(" "):
            return False
        if line.find("class") != 0 and line.find("interface") != 0 and line.find("public") != 0:
            return False
        return True

    @staticmethod
    def get_three(line, current_path, imports, root):
        source_type = None
        extends = False
        implements = False
        source = None
        dest1 = None
        dest2 = None

        class_idx = line.find("class")
        interface_idx = line.find("interface")
        extends_idx = line.find("extends")
        implements_idx = line.find("implements")
        left_brace_idx = line.find("{")

        if class_idx != -1:
            source_type = 'class'
            if extends_idx == -1 and implements_idx == -1:  # only class
                source =  line[class_idx+len('class'):left_brace_idx].strip()
            elif extends_idx != -1 and implements_idx == -1:    # extends
                source =  line[class_idx+len('class'):extends_idx].strip()
                dest1 = line[extends_idx+len('extends'):left_brace_idx].strip()
            elif extends_idx == -1 and implements_idx != -1:    # implements
                source =  line[class_idx+len('class'):implements_idx].strip()
                dest2 = line[implements_idx + len('implements'):left_brace_idx].strip()
            elif extends_idx != -1 and implements_idx != -1:
                source = line[class_idx+len('class'):extends_idx].strip()
                dest1 = line[extends_idx+len('extends'):implements_idx].strip()
                dest2 = line[implements_idx+len('implements'):left_brace_idx].strip()
        elif interface_idx != -1:
            source_type = 'interface'
            if extends_idx == -1:
                source = line[interface_idx+len('interface'):left_brace_idx].strip()
            else:
                source = line[interface_idx+len('interface'):extends_idx].strip()
                dest1 = line[extends_idx+len('extends'):left_brace_idx].strip()

        if source.find("<") != -1 and source.find(">") == -1:       # special case
            source = 'ParceledListSlice'
            dest1 = None
            dest2 = 'Parcelable'

        source = Test.cleanout(source)
        source = current_path + source
        if source not in class_hierarchy_framework.keys():
            class_hierarchy_framework[source] = Node(source_type, source)
        else:
            class_hierarchy_framework[source].set_type(source_type)

        if dest1:
            dest1 = Test.cleanout(dest1)
            dest1 = dest1.split(',')
            for i in xrange(len(dest1)):
                dest1[i] = dest1[i].strip()
                if source_type == 'interface':
                    Test.link_two('interface', source, dest1[i], current_path, imports, root)
                else:
                    Test.link_two('', source, dest1[i], current_path, imports, root)

        else:
            if source_type == 'class':
                class_hierarchy_framework[source].add_parent(class_hierarchy_framework['Ljava/lang/Object'])
                class_hierarchy_framework['Ljava/lang/Object'].add_child(class_hierarchy_framework[source])

        if dest2:
            dest2 = Test.cleanout(dest2)
            dest2 = dest2.split(",")
            for i in xrange(len(dest2)):
                dest2[i] = dest2[i].strip()
                Test.link_two('interface', source, dest2[i], current_path, imports, root)

    @staticmethod
    def link_two(target_type, source, dest, current_path, imports, root):
        get_destination = False
        for im in imports:
            if im.endswith(dest):
                get_destination = True
                dest = im
                break
        # dest1 can be found in imports
        if get_destination:
            if dest in class_hierarchy_framework.keys():
                class_hierarchy_framework[source].add_parent(class_hierarchy_framework[dest])
                class_hierarchy_framework[dest].add_child(class_hierarchy_framework[source])
                if target_type == 'interface':
                    class_hierarchy_framework[dest].set_type("interface")
        else:
            # dest1 can be found in current package
            if os.path.isfile(root + os.sep + dest + '.java'):
                dest = current_path + dest
                class_hierarchy_framework[source].add_parent(class_hierarchy_framework[dest])
                class_hierarchy_framework[dest].add_child(class_hierarchy_framework[source])
                if target_type == 'interface':
                    class_hierarchy_framework[dest].set_type("interface")
            else:
                if "Ljava/lang/" + dest in class_hierarchy_framework.keys():
                    dest = "Ljava/lang/" + dest
                    class_hierarchy_framework[source].add_parent(class_hierarchy_framework[dest])
                    class_hierarchy_framework[dest].add_child(class_hierarchy_framework[source])
                    if target_type == 'interface':
                        class_hierarchy_framework[dest].set_type("interface")
                else:
                    # special case
                    if dest.find("java.lang") != -1:
                        if dest.find("RuntimeException") != -1:
                            class_hierarchy_framework[source].add_parent(class_hierarchy_framework["Ljava/lang/RuntimeException"])
                            class_hierarchy_framework['Ljava/lang/RuntimeException'].add_child(class_hierarchy_framework[source])
                            if target_type == 'interface':
                                class_hierarchy_framework[dest].set_type("interface")
                        elif dest.find("Exception") != -1:
                            class_hierarchy_framework[source].add_parent(class_hierarchy_framework["Ljava/lang/Exception"])
                            class_hierarchy_framework['Ljava/lang/Exception'].add_child(class_hierarchy_framework[source])
                            if target_type == 'interface':
                                class_hierarchy_framework[dest].set_type("interface")
                    else:
                        # dest is the full path
                        if dest.find(".") != -1:
                            dest = 'L' + '/'.join(dest.split('.'))
                            if dest in class_hierarchy_framework.keys():
                                class_hierarchy_framework[source].add_parent(class_hierarchy_framework[dest])
                                class_hierarchy_framework[dest].add_child(class_hierarchy_framework[source])
                                if target_type == 'interface':
                                    class_hierarchy_framework[dest].set_type("interface")
                        # there are many inner class, we just ignore them
    @staticmethod
    def get_class():
        org = [input_directory]
        while org:
            dst = []
            for directory in org:
                for root, dirs, files in os.walk(directory):
                    for fi in files:
                        if fi and fi.endswith(".java"):
                            pwd = root + os.sep + fi
                            idx = pwd.find(parent_directory)
                            cl = 'L' + pwd[idx+len(parent_directory):-5]
                            class_hierarchy_framework[cl] = Node('class', cl)
                    for di in dirs:
                        dst.append(di)
            org = dst

    @staticmethod
    def cleanout(cl):
        while cl and cl.find('<') != -1:
            cl = cl[:cl.find('<')] + cl[cl.find('>')+1:]
        return cl

if __name__ == "__main__":
    wf = open('logs.txt', 'a+')
    sys.stdout = wf

    T = Test()
    T.get_class()

    T.parse_file_in_directory()

    # put the class hierarchy tree into file
    for key in class_hierarchy_framework.keys():
        cur_node = class_hierarchy_framework[key]
        has_implements = False
        has_extends = False

        if cur_node.type == 'class':
            print 'class ' + key
        else:
            print 'interface ' + key
        parents = cur_node.parents

        for p in parents:
            if p.type == 'class':
                has_extends = True
            if p.type == 'interface':
                has_implements = True

        if has_extends:
            print '     extends ',
            for p in parents:
                if cur_node.type == 'class' and p.type == 'class':
                    print p.name
                if cur_node.type == 'interface' and p.type == 'interface':
                    print p.name

        if has_implements:
            print '     implements ',
            for p in parents:
                if p.type == 'interface':
                    print p.name,
            print

