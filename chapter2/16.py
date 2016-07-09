#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

n = int(sys.argv[1])

lineCount = 0
with open('hightemp.txt', 'r') as f:
    for line in f:
        lineCount += 1

linePerFile = lineCount // n + 1
with open('hightemp.txt', 'r') as f:
    for i in range(n):
        with open('hightemp{}.txt'.format(i), 'w') as f0:
            for j in range(linePerFile):
                if i * linePerFile + j + 1 <= lineCount:
                    f0.write(f.readline())