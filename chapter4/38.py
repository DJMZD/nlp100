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

w = 0.5
plt.hist([count for word, count in word_dict.items()],
                bins = 50, range = (0, 100))
plt.show()