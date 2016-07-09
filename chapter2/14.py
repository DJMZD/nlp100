#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

n = int(sys.argv[1])

with open('hightemp.txt') as f:
    l = f.read().split('\n')[:n]
    for m in l:
        print(m)