#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from operator import itemgetter

d = defaultdict(int)
with open('hightemp.txt', 'r') as f:
    for line in f:
        d[line.split()[0]] += 1
for k in sorted(d.items(), key = itemgetter(1), reverse = True):
    print(k[0], k[1])