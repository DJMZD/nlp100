#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

article = []
with open('neko.txt.mecab', 'r') as f:
    sent = []
    for line in f:
        if line == 'EOS\n':
            if len(sent) != 0:
                article.append(sent)
                sent = []
        else:
            surface, info = line.split('\t')
            sent.append({'surface': surface,
                         'base': info.split(',')[6],
                         'pos': info.split(',')[0],
                         'pos1': info.split(',')[1]})

with open('neko.txt.mecab.pickle', 'wb') as f:
    pickle.dump(article, f)