#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


# split the big file ImplicitEdges.txt into 100 files

if not os.path.exists("Implicit"):
    os.makedirs('Implicit')
for i in xrange(1, 103):
    with open("Implicit/" + str(i) + ".txt", 'w') as f:
        pass

count = 0
filenum = 1
with open('../../tools/EdgeMiner/ImplicitEdges.txt') as bigfile:
    for line in bigfile:
        with open("Implicit/" + str(filenum) + ".txt", 'a') as smallfile:
            smallfile.write(line)
        count += 1
        if count == 50000:
            count = 0
            filenum += 1