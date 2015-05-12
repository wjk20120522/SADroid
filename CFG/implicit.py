#!/usr/bin/python
# -*- coding: utf-8 -*-

def readfile():
    with open('test.txt', 'r') as f:
        for line in f:
            print line,

if __name__ == '__main__':

    with open('../tools/EdgeMiner/ImplicitEdges.txt', 'r') as f:
      for line in f:
          if line.find("android.app.Activity.onPause:") != -1 :
              print line,
          if line.find("android.app.Activity.onStop:") != -1 :
              print line,
          if line.find("android.app.Activity.onDestroy:") != -1 :
              print line,





