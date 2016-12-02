#!/usr/bin/env python
# -*- coding=utf8 -*-
# https://github.com/kn45/SegJb

import os
import sys
try:
    sys.path.append('../')
except:
    pass
from segjb import SegJb

segutil = SegJb()
segutil.init(stopwords_file=SegJb.DEFAULT_STPW,
             puncs_file=SegJb.DEFAULT_PUNC,
             user_dict=SegJb.DEFAULT_DICT,
             silent=True)
segutil.set_param(delim=' ', ngram=2, keep_stopwords=True, keep_puncs=False)

test_corps = [
    '我来到北京清华大学',
    '小明硕士毕业于中国科学院计算所，后在日本京都大学深造',
    '他来到了网易杭研大厦',
    '网易']
for line in test_corps:
    fields = line.strip('\n').split('\t')
    corpus = fields[0]
    seg_str = segutil.cut2str(corpus)
    fields[0] = seg_str.encode('utf-8')
    print '\t'.join(fields)
