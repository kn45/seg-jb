# SegJb

Segmentation wrapper of [Jieba](https://github.com/fxsjy/jieba) Chinese segmentation.  
https://github.com/kn45/SegJb  
`pip install segjb` (dependency: jieba) 

- Lazy initialization.  
- Initialization with user defined dict.  
- Build-in stop-words dict, punctuations dict.  
- Output control of stopwords, punctuations, minimum word length, output delimiters etc..  
- Support ngram.  

## API

**init(stopwords_file, puncs_file, user_dict, silent, main_dict, thread)**  
-- Initialize the segmentation utility instance.  
- return: void.  
- stopwords_file: stopword dictionary. Use "" to disable. [SegJb.DEFAULT_STPW]  
- puncs_file: punctuation dictionary. Use "" to disable. [SegJb.DEFAULT_PUNC]  
- user_dict: load user customized dictionary. Use "" to disable. [SegJb.DEFAULT_DICT]  
- silent: whether print initializing log. [True]  
- thread: number of part to separate the corpus for parallel. [1]
  ​

**set_param(delim, min_word_len, ngram, keep_stopwords, keep_puncs)**  
-- Set one or more parameters of the segmentation utility instance. Refer to parameter description.  
- return: void  
  ​

**cut2list(corp)**  
-- Cut a sentence to list due to configuration.  
- return: list<unicode word>  
- corp: unicode or utf8 sentence.  
  ​

**cut2str(corp)**  
-- Cut a sentence to a delimeter(can be set by set_param) joined string.  
- return: unicode string.  
- corp: unicode or utf8 sentence.  
  ​

## Parameters

- delim [' ']  
  the delimeter used to constuct the segmentation result in string.  

- min_word_len [1]  
  word with length less than min_word_len will not in segmentation result.  

- ngram [1]  
  result can be ngram.  

- keep_stopwords [True]  
  whether to keep stopwords in result.  

- keep_puncs [True]  
  whether to keep stopwords in result.  


## Example:

```python
from segjb import SegJb
hdl_seg = SegJb()
hdl_seg.init()
hdl_seg.set_param(delim=' ', ngram=2, keep_stopwords=True, keep_puncs=False)
print hdl_seg.cut2str('这是一场精彩的比赛')
```

## Reference:

- [Bigdict](https://github.com/qinwf/BigDict) from iLife(562193561@qq.com)
