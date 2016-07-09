#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('hightemp.txt', 'r') as f:
    l = f.read().replace('\t', ' ')

with open('hightemp.txt', 'w') as f:
    f.write(l)