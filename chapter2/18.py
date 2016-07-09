#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter

lines = []
with open('hightemp.txt', 'r') as f:
    for line in f:
        lines.append(line.split())
for l in sorted(lines, key = itemgetter(2), reverse = True):
    for w in l:
        print(w, end = ' ')
    print()