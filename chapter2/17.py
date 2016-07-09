#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = set()
with open('hightemp.txt', 'r') as f:
    for line in f:
        s.add(line.split()[0])
for k in sorted(s):
    print(k)