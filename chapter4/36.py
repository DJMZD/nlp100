#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from operator import itemgetter
import pickle

word_dict = defaultdict(int)
with open('neko.txt.mecab.pickle', 'rb') as f:
    article = pickle.load(f)
    for sent in article:
        for word in sent:
            word_dict[word['base']] += 1

for w, n in sorted(word_dict.items(), key = itemgetter(1), reverse = True)[:10]:
    print(w, n)