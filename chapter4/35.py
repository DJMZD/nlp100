#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

longest_cont = []
with open('neko.txt.mecab.pickle', 'rb') as f:
    article = pickle.load(f)
    for sent in article:
        n_cont = []
        for i in range(len(sent)):
            if sent[i]['pos'] == '名詞':
                n_cont.append(sent[i]['surface'])
            else:
                if len(n_cont) > len(longest_cont):
                    longest_cont = n_cont
                n_cont = []

print(longest_cont)