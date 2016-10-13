# -*- coding=utf-8 -*-
import jieba


class SegJb(object):
    def __init__(self):
        self.stopwords = {}
        self.puncs = {}
        self.min_word_cnt = 0
        self.delim = ' '
        self.keep_stopwords = True
        self.keep_puncs = True

    def init(self, stopwords_file=None, puncs_file=None):
        jieba.initialize()
        if stopwords_file is not None:
            with open(stopwords_file) as f:
                self.stopwords = {x.rstrip('\n').decode('utf8'): ''
                                  for x in f.readlines()}
        if puncs_file is not None:
            with open(puncs_file) as f:
                self.puncs = {x.rstrip('\n').decode('utf8'): ''
                              for x in f.readlines()}

    def set_param(self, min_word_cnt=None, delim=None, keep_stopwords=None,
                  keep_puncs=None):
        if isinstance(min_word_cnt, int):
            self.min_word_cnt = min_word_cnt
        if isinstance(delim, str):
            self.delim = delim
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
        if not self.keep_stopwords:
            segs = [x for x in segs if x not in self.stopwords]
        if not self.keep_puncs:
            segs = [x for x in segs if x not in self.puncs]
        return segs

    def cut2str(self, corp):
        segs = jieba.cut(corp)
        if not self.keep_stopwords:
            segs = [x for x in segs if x not in self.stopwords]
        if not self.keep_puncs:
            segs = [x for x in segs if x not in self.puncs]
        return self.delim.join(segs)


def test():
    segutil = SegJb()
    segutil.init('./stopwords.dat', './punctuations.dat')
    segutil.set_param(delim=' ', keep_stopwords=False, keep_puncs=False)
    # segutil.debug()
    print segutil.cut2list('测试一下,效果怎么样,万一')
    print segutil.cut2str('测试一下,效果怎么样,万一')

if __name__ == '__main__':
    test()
