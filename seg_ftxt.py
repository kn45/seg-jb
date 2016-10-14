#!/usr/bin/env python
# -*- coding=utf8 -*-
# https://github.com/kn45/SegJb

import os
import segjb
import sys

seg_dir = sys.path[0]
segutil = segjb.SegJb()
segutil.init(stopwords_file=seg_dir+'/stopwords.dat',
             puncs_file=seg_dir+'/punctuations.dat',
             user_dict=seg_dir+'/newdict.dat')
segutil.set_param(delim=' ', ngram=2, keep_stopwords=True, keep_puncs=False)

for line in sys.stdin:
    fields = line.strip('\n').split('\t')
    corpus = fields[0]
    seg_str = segutil.cut2str(corpus)
    fields[0] = seg_str.encode('utf-8')
    print '\t'.join(fields)
