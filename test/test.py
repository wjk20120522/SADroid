#!/usr/bin/env python
# -*- coding:utf-8  -*-

import sys
import string
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

import fileinput

for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print '%-75s # %2i' %(line, num)
exit()

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(nextX-state[i]) in (0, nextY-i):
            return True
    return False

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos, )
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


print len(list(queens(16)))

exit()

d = Drawing(100, 100)
s = String(50, 50, 'Hello, world!dddddddddddddsad./t', textAnchor='middle')

d.add(s)
renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')