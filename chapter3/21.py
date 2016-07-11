#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

p = re.compile(r'\[\[Category\:.+\]\]')
with open('english-article.txt', 'r') as f:
    for line in f:
        if p.search(line):
            print(line.strip('\n'))