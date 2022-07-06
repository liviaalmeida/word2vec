# word2vec

This repo contains some exercices about creating [word2vec](https://en.wikipedia.org/wiki/Word2vec) models using the library [gensim](https://github.com/RaRe-Technologies/gensim).

## Files

### analogies

File containing some sample analogies to be tested by a trained model.

### analogies.py

Makes analogies of the form `man woman king` (expected output: `queen`) using a trained model - so it is a KeyedVectors model. The model should be supplied as a parameter. An optional parameter is a file containing analogies, and then every analogy is show, the program halts and waits any user input. After the file is processed the program defaults to typed analogies - or goes straight to this part if no file is suplied.

```[sh]
python analogies.py [keyed-vectors-model] [analogies-text-file]
```

### gameofthrones.txt

Sample containing the 5 Game of Thrones books. Useful to train models and run experiments.

### model.py

Creates a model based on a simple text file, which is supplied as a parameter. The output is a keyed vectors model (so non-trainable) in the form of file name and the extension `.wv`.

```[sh]
python model.py [sample-textfile]
```


### wiki.py

Creates a model based on a Wikipedia Corpus of articles - the file has to be supplied as a parameter. It saves the resulting vectors in a file called `wiki.wv`. The dumps can be download from [here](https://dumps.wikimedia.org/backup-index.html) in the form of `[LANG]wiki-[DATE]-pages-articles-multistream.xml.bz2`. It takes a long time.

```[sh]
python wiki.py [wikipedia-dump-file.xml.bz2]
```

## Resources

- [NLPL word embeddings repository](http://vectors.nlpl.eu/repository/)

- [Paper introducing word2vec](https://arxiv.org/pdf/1301.3781.pdf)

- [Paper expanding word2vec](https://proceedings.neurips.cc/paper/2013/file/9aa42b31882ec039965f3c4923ce901b-Paper.pdf)
