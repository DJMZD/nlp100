#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

p = re.compile(r'(\'{5}|\'{3})(.+?)\1')
with open('english-article.txt', 'r') as f:
    for line in f:
        print(p.sub(r'\2', line.strip('\n')))