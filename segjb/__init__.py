# -*- coding=utf-8 -*-
"""A wrapper for jieba segmentation
For full documentation, refer to https://github.com/kn45/SegJb/README.md
Quick Start:
    from segjb import SegJb
    segutil = SegJb()
    segutil.init()
    segutil.set_param(delim=' ', keep_stopwords=False, keep_puncs=False)
    print segutil.cut2list('测试一下,效果怎么样,万一')
    print segutil.cut2str('测试一下,效果怎么样,万一')
"""
import jieba
import logging
import os


class SegJb(object):
    """Wrapper for Jieba
    """
    MODULE_REAL_DIR = os.path.dirname(os.path.realpath(__file__))
    DEFAULT_STPW = MODULE_REAL_DIR + '/stopwords.dat'
    DEFAULT_PUNC = MODULE_REAL_DIR + '/punctuations.dat'
    DEFAULT_DICT = MODULE_REAL_DIR + '/newdict.dat'

    def __init__(self):
        self.stopwords = {}
        self.puncs = {}
        self.delim = ' '
        self.min_word_len = 1
        self.ngram = 1
        self.keep_stopwords = True
        self.keep_puncs = True

    def init(self, stopwords_file=None, puncs_file=None, user_dict=None,
             silent=None):
        # set default value, cat wrong value to default
        if not isinstance(stopwords_file, str):
            stopwords_file = SegJb.DEFAULT_STPW
        if not isinstance(puncs_file, str):
            puncs_file = SegJb.DEFAULT_PUNC
        if not isinstance(user_dict, str):
            user_dict = SegJb.DEFAULT_DICT
        if not isinstance(silent, bool):
            silent = True

        # init due to settings
        if silent:
            jieba.setLogLevel(logging.ERROR)
        jieba.initialize()
        if user_dict != '':
            jieba.load_userdict(user_dict)
        if stopwords_file != '':
            with open(stopwords_file) as f:
                self.stopwords = {x.rstrip('\n').decode('utf8'): ''
                                  for x in f.readlines()}
        if puncs_file != '':
            with open(puncs_file) as f:
                self.puncs = {x.rstrip('\n').decode('utf8'): ''
                              for x in f.readlines()}

    def set_param(self, delim=None, min_word_len=None, ngram=None,
                  keep_stopwords=None, keep_puncs=None):
        if isinstance(delim, str):
            self.delim = delim
        if isinstance(min_word_len, int):
            self.min_word_len = min_word_len
        if isinstance(ngram, int):
            self.ngram = ngram
        if isinstance(keep_stopwords, bool):
            self.keep_stopwords = keep_stopwords
        if isinstance(keep_puncs, bool):
            self.keep_puncs = keep_puncs

    def debug(self):
        print self.__dict__
        print len(self.stopwords)
        print len(self.puncs)

    def cut2list(self, corp):
        segs = jieba.cut(corp)
        segs = [x for x in segs if len(x) >= self.min_word_len]
        if not self.keep_stopwords:
            segs = [x for x in segs if x not in self.stopwords]
        if not self.keep_puncs:
            segs = [x for x in segs if x not in self.puncs]
        ngram_segs = []
        for i, seg in enumerate(segs):
            nseg = seg
            for j in xrange(i, min(i+self.ngram-1, len(segs)-1)):
                # j+1 is the offset
                nseg += segs[j+1]
                ngram_segs.append(nseg)
        segs += ngram_segs
        return segs

    def cut2str(self, corp):
        segs = jieba.cut(corp)
        segs = [x for x in segs if len(x) >= self.min_word_len]
        if not self.keep_stopwords:
            segs = [x for x in segs if x not in self.stopwords]
        if not self.keep_puncs:
            segs = [x for x in segs if x not in self.puncs]
        ngram_segs = []
        for i, seg in enumerate(segs):
            nseg = seg
            for j in xrange(i, min(i+self.ngram-1, len(segs)-1)):
                # j+1 is the offset
                nseg += segs[j+1]
                ngram_segs.append(nseg)
        segs += ngram_segs
        return self.delim.join(segs)


def test():
    segutil = SegJb()
    print SegJb.DEFAULT_STPW
    print SegJb.DEFAULT_PUNC
    print SegJb.DEFAULT_DICT
    segutil.init()
    segutil.set_param(delim=' ', keep_stopwords=False, keep_puncs=False)
    # segutil.debug()
    print segutil.cut2list('测试一下,效果怎么样,万一')
    print segutil.cut2str('测试一下,效果怎么样,万一')

if __name__ == '__main__':
    test()
