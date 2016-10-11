#!/usr/bin/env python
# -*- coding=utf8 -*-

import jieba
import os
import sys

seg_dir = sys.path[0]
# seg auto initialize here due to load user_dict
# manually initialize if needed when there's no user_dict
# jieba.set_dictionary('data/dict.txt.big')  # set main dict(optional)
# jieba.initialize()
jieba.load_userdict(seg_dir + '/newdict.dat')

stop_words = {}
puncs = {}
with open(seg_dir + '/stopwords.dat') as f:
    stop_words = {x.rstrip('\n').decode('utf8'): '' for x in f.readlines()}
with open(seg_dir + '/punctuations.dat') as f:
    puncs = {x.rstrip('\n').decode('utf8'): '' for x in f.readlines()}

for line in sys.stdin:
    fields = line.strip('\n').split('\t')
    corpus = fields[0]
    segs_raw = jieba.cut(corpus)
    segs_cln = [x for x in segs_raw if x not in puncs]
    fields[0] = ' '.join(segs_cln).encode('utf8')
    print '\t'.join(fields)
