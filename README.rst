SegJb
=====

| Segmentation wrapper of `Jieba <https://github.com/fxsjy/jieba>`__
  Chinese segmentation.
|  https://github.com/kn45/SegJb

-  | Lazy initialization.

-  | Initialization with user defined dict.

-  | Build-in stop-words dict, punctuations dict.

-  | Output control of stopwords, punctuations, minimum word length,
     output delimiters etc..

-  | Support ngram.

API
---

| **init(stopwords\_file, puncs\_file, user\_dict, silent, main\_dict,
  thread)**
|  -- Initialize the segmentation utility instance.

-  | return: void.

-  | stopwords\_file: stopword dictionary. Use "" to disable.
     [SegJb.DEFAULT\_STPW]

-  | puncs\_file: punctuation dictionary. Use "" to disable.
     [SegJb.DEFAULT\_PUNC]

-  | user\_dict: load user customized dictionary. Use "" to disable.
     [SegJb.DEFAULT\_DICT]

-  | silent: whether print initializing log. [True]

-  thread: number of part to separate the corpus for parallel. [1]

| **set\_param(delim, min\_word\_len, ngram, keep\_stopwords,
  keep\_puncs)**
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

-  | delim [' ']
   |  the delimeter used to constuct the segmentation result in string.

-  | min\_word\_len [1]
   |  word with length less than min\_word\_len will not in segmentation
     result.

-  | ngram [1]
   |  result can be ngram.

-  | keep\_stopwords [True]
   |  whether to keep stopwords in result.

-  | keep\_puncs [True]
   |  whether to keep stopwords in result.

Example:
--------

.. code:: python

    from segjb import SegJb
    hdl_seg = Segjb()
    hdl_seg.init()
    hdl_seg.set_param(delim=' ', ngram=2, keep_stopwords=True, keep_puncs=False)
    print hdl_seg.cut2str('这是一场精彩的比赛')
