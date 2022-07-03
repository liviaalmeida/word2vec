from sys import argv
import re
import nltk
from gensim.models import Word2Vec

re_quotes = re.compile(r'["\']', re.UNICODE)
re_number = re.compile(r'\d+', re.UNICODE)
re_allow = re.compile(r'\w', re.UNICODE)
re_trim = re.compile(r' +', re.UNICODE)

def preprocessor(text):
  text = text.lower()
  text = re_trim.sub(' ', text)
  text = re_number.sub('NUMBER', text)
  
  phrases = text.split('.')
  tokensLists = [nltk.wordpunct_tokenize(phrase) for phrase in phrases]
  textOnly = [list(filter(re_allow.search, tokensList)) for tokensList in tokensLists]
  filtered = list(filter(lambda lst: len(lst) > 0, textOnly))

  return filtered

with open('gameofthrones.txt', 'r', encoding='utf8') as textFile:
  text = textFile.readlines()
  text = ' '.join(text)

sentences = preprocessor(text)


if __name__ == "__main__":
  if len(argv) == 2:
    with open(argv[1], 'r', encoding='utf8') as textFile:
      text = textFile.readlines()
      text = ' '.join(text)
    sentences = preprocessor(text)
    model = Word2Vec(sentences=sentences, vector_size=100, window=5, min_count=3, workers=4)
    fileName = argv[1].split('.')[0]
    model.wv.save(f'{fileName}.wv')