import os
import random

class RandomWordGenerator:

  def __init__(self):
    self.words = []
    dictionary = open(os.path.join(os.path.dirname(__file__), 'files/dictionary.txt'), 'r')
    for word in dictionary:
      self.words.append(word.rstrip())

  def get_some_random_words(self, n=1):
    results = []
    for i in range(n):
      results.append(self.words[random.randint(0, n - 1)])
    return results
