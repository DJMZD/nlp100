#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

with open('neko.txt.mecab.pickle', 'rb') as f:
    article = pickle.load(f)
    for sent in article:
        for word in sent:
            if word['pos1'] == 'サ変接続':
                print(word['surface'])