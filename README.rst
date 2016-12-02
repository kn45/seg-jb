SegJb
=====

| Segmentation wrapper of `Jieba <https://github.com/fxsjy/jieba>`__
  Chinese segmentation.
|  https://github.com/kn45/SegJb

-  | Lazy initialization.

-  | Initialization with customized main dict and user defined dict.

-  | Build-in stop-words dict, punctuations dict.

-  | Output control of stopwords, punctuations, minimum word length,
     output delimiters etc..

-  | Support ngram.

API
---

| **init(stopwords\_file=None, puncs\_file=None, user\_dict=None,
  silent=None, main\_dict=None)**
|  -- Initialize the segmentation utility instance.

-  | return: void.

-  | stopwords\_file: stopword dictionary. Use SegJb.DEFAULT\_STPW for
     built-in.

-  | puncs\_file: punctuation dictionary. Use SegJb.DEFAULT\_PUNC for
     built-in.

-  | user\_dict: load user customized dictionary. Use
     SegJb.DEFAULT\_DICT for built-in.

-  | silent: whether print initializing log.

-  | main\_dict: initialize with another main dictionary, default one is
     Jieba built-in dictionary.
   | 

| **set\_param(delim=None, min\_word\_len=None, ngram=None,
  keep\_stopwords=None, keep\_puncs=None)**
|  -- Set one or more parameters of the segmentation utility instance.
  Refer to parameter description.

-  | return: void
   | 

| **cut2list(corp)**
|  -- Cut a sentence to list due to configuration.

-  | return: list

-  | corp: unicode or utf8 sentence.
   | 

| **cut2str(corp)**
|  -- Cut a sentence to a delimeter(can be set by set\_param) joined
  string.

-  | return: unicode string.

-  | corp: unicode or utf8 sentence.
   | 

Parameters
----------

-  | delim [default=' ']
   |  the delimeter used to constuct the segmentation result in string.

-  | min\_word\_len [default=1]
   |  word with length less than min\_word\_len will not in segmentation
     result.

-  | ngram [default=1]
   |  result can be ngram.

-  | keep\_stopwords [default=True]
   |  whether to keep stopwords in result.

-  | keep\_puncs [default=True]
   |  whether to keep stopwords in result.

Example:
--------

.. code:: python

    from segjb import SegJb
    hdl_seg = Segjb()
    hdl_seg.init(stopwords_file=SegJb.DEFAULT_STPW,
                 puncs_file=SegJb.DEFAULT_PUNC,
                 user_dict=SegJb.DEFAULT_DICT)
    hdl_seg.set_param(delim=' ', ngram=2, keep_stopwords=True, keep_puncs=False)
    print hdl_seg.cut2str('这是一场精彩的比赛')
