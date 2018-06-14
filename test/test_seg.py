#!/usr/bin/env python
# -*- coding=utf8 -*-
# https://github.com/kn45/SegJb

from __future__ import print_function
import os
import sys
import time
try:
    sys.path.append('../')
except:
    pass
from segjb import SegJb

segutil = SegJb()
segutil.init(silent=False, thread=2)
segutil.set_param(delim=' ', ngram=1, keep_stopwords=True, keep_puncs=False)

test_corpus_1 = [
    u'我来到北京清华大学',
    u'小明硕士毕业于中国科学院计算所，后在日本京都大学深造',
    u'他来到了网易杭研大厦',
    u'网易']

for line in test_corpus_1:
    fields = line.strip('\n').split('\t')
    corpus = fields[0]
    fields[0] = segutil.cut2str(corpus)
    print('\t'.join(fields))

st_time = time.time()
with open('test_corp') as f:
    segutil.cut2list(f.read())
print(str(time.time() - st_time))
