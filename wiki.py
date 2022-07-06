from sys import argv
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def createmodel(sentences):
  workers = max(1, multiprocessing.cpu_count() - 1)
  word2vec = Word2Vec(None, min_count=10, sample=1E-3, sg=1, window=10, workers=workers, vector_size=500)
  word2vec.build_vocab(sentences)
  word2vec.train(sentences)
  return word2vec

if __name__ == "__main__":
  if len(argv) == 2:
    sentences = LineSentence(argv[1])
    word2vec = createmodel(sentences)
    word2vec.wv.save('wiki.wv')