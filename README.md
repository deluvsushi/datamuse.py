# datamuse.py
Web-API for [datamuse.com](https://www.datamuse.com) website which is word-finding query engine for developers

## Example
```python
import datamuse
datamuse = datamuse.Datamuse()
words_with_similar_meaning = datamuse.get_words_with_similar_meaning(word="")
print(words_with_similar_meaning)
```
