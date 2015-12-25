#!/usr/bin/env python

import sys
sys.path.append("../")

from androguard.session import Session

TEST = "/Users/wjk/Desktop/app-release.apk"


def display_CFG(d, dx, classes):
    # d: DalvikVMFormat
    # dx: newVMAnalysis
    count = 0
    for method in d.get_methods():

        g = dx.get_method_novm(method)
        count += 1
        for i in g.basic_blocks.get():
            print "\t %s %x %x" % (i.name, i.start, i.end),\
                '[ NEXT = ', ', '.join("%x-%x-%s" % (j[0], j[1], j[2].get_name()) for j in i.childs), ']', \
                '[ PREV = ', ', '.join(j[2].get_name() for j in i.fathers), ']'

s = Session()
with open(TEST, "r") as fd:
    s.add(TEST, fd.read())

a, d, dx = s.get_objects_apk(TEST)

classes = d.get_classes_names()

display_CFG(d, dx, classes)

