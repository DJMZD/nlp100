#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

with open('neko.txt.mecab.pickle', 'rb') as f:
    article = pickle.load(f)
    for sent in article:
        for i in range(1, len(sent) - 1):
            word_prev = sent[i - 1]
            word = sent[i]
            word_next = sent[i + 1]
            if word_prev['pos'] == '名詞' and \
                word['surface'] == 'の' and \
                word_next['pos'] == '名詞':
                    print(word_prev['surface'] +
                          word['surface'] +
                          word_next['surface'])