#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter, defaultdict
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
import pickle

word_dict = defaultdict(int)
with open('neko.txt.mecab.pickle', 'rb') as f:
    article = pickle.load(f)
    words = [w['base'] for sent in article for w in sent]
    word_dict = Counter(words)

word_list = sorted(word_dict.items(), key = itemgetter(1), reverse = True)
rank = np.arange(len(word_list)) + 1
count = [c for w, c in word_list]

plt.plot(rank, count)
plt.xscale('log')
plt.yscale('log')
plt.show()