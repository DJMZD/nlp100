#!/usr/bin/env python
# -*- coding: utf-8 -*-

import regex

# TO IMPROVE
p = regex.compile(r'(?<rec>\{(?:[^{}]+|(?&rec))*\})')
with open('english-article.txt', 'r') as f:
    f.readline()
    line = f.read()
    m = p.search(line)
    if m:
        print(m.group('rec'))