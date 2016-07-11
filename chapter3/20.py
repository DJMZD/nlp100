#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import json

text = ''
with gzip.open ('jawiki-country.json.gz', 'rb') as f_in:
    with open('jawiki-country.json', 'wb') as f_out:
        f_out.writelines(f_in)
with open('jawiki-country.json', 'r') as f:
    for line in f.readlines():
        data = json.loads(line)
        if data['title'] == u'イギリス':
            text = data['text']
with open('english-article.txt', 'w') as f_w:
    f_w.write(text)