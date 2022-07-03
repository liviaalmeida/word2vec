from sys import argv
import multiprocessing
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec

if __name__ == "__main__":
  if len(argv) == 2:
    wiki = WikiCorpus(argv[1], dictionary={})
    sentences = list(wiki.get_texts())
    workers = max(1, multiprocessing.cpu_count() - 1)
    word2vec = Word2Vec(sentences, vector_size=200, window=10, min_count=10, workers=workers, sample=1E-3)
    word2vec.wv.save('wiki.wv')