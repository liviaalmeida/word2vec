# word2vec

This repo contains some exercices about creating [word2vec](https://en.wikipedia.org/wiki/Word2vec) models using the library [gensim](https://github.com/RaRe-Technologies/gensim).

## Files

### gameofthrones.txt

Sample containing the 5 Game of Thrones books. Useful to train models and run experiments.

### model.py

Creates a model based on a simple text file. The only argument is the file and the output is a keyed vectors model (so non-trainable) in the form of file name and the extension `.wv`.
