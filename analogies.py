from gensim.models import KeyedVectors
from sys import argv

def analogiesFromFile(fileName, model):
  analogies = []
  with open(fileName) as f:
    lines = f.readlines()
    for line in lines:
      analogies.append(line.strip().split(' '))
  for analogy in analogies:
    print('analogy: ', *analogy)
    print(*model.most_similar(negative=[analogy[0]], positive=[analogy[1], analogy[2]]), '\n', sep='\n')
    input()

def getAnalogies(model):
  prompt = 'Type 3 words: '
  inp = input(prompt)
  while(inp != ''):
    words = inp.split(' ')
    while len(words) != 3:
      print(f'There was a mistake!', end='\n')
      inp = input(prompt)
      words = inp.split(' ')
    try:
      print(*model.most_similar(negative=[words[0]], positive=[words[1], words[2]]), sep='\n')
    except KeyError as err:
      print(err)
    inp = input(prompt)

if __name__ == '__main__':
  model = KeyedVectors.load_word2vec_format(argv[1], binary=False)
  if len(argv) > 2:
    analogiesFromFile(argv[2], model)
  getAnalogies(model)
