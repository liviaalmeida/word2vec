from sys import argv
import multiprocessing
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec

def getsentences(corpus):
  sentences = []
  for index, sentence in enumerate(corpus.get_texts()):
    sentences.append(sentence)
    if index % 10000 == 0:
      print(f'Processed {index} texts')
  print(f'Finished. Processed {len(sentences)} texts')
  return sentences

def createmodel(sentences):
  workers = max(1, multiprocessing.cpu_count() - 1)
  word2vec = Word2Vec(sentences, vector_size=200, window=10, min_count=10, workers=workers, sample=1E-3)
  return word2vec

if __name__ == "__main__":
  if len(argv) == 2:
    wiki = WikiCorpus(argv[1], dictionary={}, processes=1, lower=True)
    sentences = getsentences(wiki)
    word2vec = createmodel(sentences)
    word2vec.wv.save('wiki.wv')