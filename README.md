# SegJb
Segmentation wrapper of [Jieba](https://github.com/fxsjy/jieba) Chinese segmentation.  
https://github.com/kn45/SegJb

- Lazy initialization.  
- Initialization with customized main dict and user defined dict.  
- Build-in stop-words dict, punctuations dict.  
- Output control of stopwords, punctuations, minimum word length, output delimiters etc..  
- Support ngram.  

## API

**init(stopwords_file=None, puncs_file=None, user_dict=None, silent=None, main_dict=None)**  
-- Initialize the segmentation utility instance.  
- return: void.  
- stopwords_file: stopword dictionary. Use SegJb.DEFAULT_STPW for built-in.  
- puncs_file: punctuation dictionary. Use SegJb.DEFAULT_PUNC for built-in.  
- user_dict: load user customized dictionary. Use SegJb.DEFAULT_DICT for built-in.  
- silent: whether print initializing log.  
- main_dict: initialize with another main dictionary, default one is Jieba built-in dictionary.  
  ​

**set_param(delim=None, min_word_len=None, ngram=None, keep_stopwords=None, keep_puncs=None)**  
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

- delim [default=' ']  
  the delimeter used to constuct the segmentation result in string.  

- min_word_len [default=1]  
  word with length less than min_word_len will not in segmentation result.  

- ngram [default=1]  
  result can be ngram.  

- keep_stopwords [default=True]  
  whether to keep stopwords in result.  

- keep_puncs [default=True]  
  whether to keep stopwords in result.  


## Example:

```python
from segjb import SegJb
hdl_seg = Segjb()
hdl_seg.init(stopwords_file=SegJb.DEFAULT_STPW,
             puncs_file=SegJb.DEFAULT_PUNC,
             user_dict=SegJb.DEFAULT_DICT)
hdl_seg.set_param(delim=' ', ngram=2, keep_stopwords=True, keep_puncs=False)
print hdl_seg.cut2str('这是一场精彩的比赛')
```
