#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

with open('neko.txt.mecab.pickle', 'rb') as f:
    article = pickle.load(f)
    for sent in article:
        for word in sent:
            if word['pos'] == '動詞':
                print(word['surface'])