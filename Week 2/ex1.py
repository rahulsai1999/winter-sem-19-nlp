from nltk.corpus import brown
from nltk.corpus import inaugural
from nltk.book import *

# brown
categories = brown.categories()
words = brown.words(categories='adventure')

# inagural
files = inaugural.fileids()
lincoln = inaugural.words(fileids='1865-Lincoln.txt')
obama = inaugural.words(fileids='2009-Obama.txt')
trump = inaugural.words(fileids='2017-Trump.txt')
carter = inaugural.words(fileids='1977-Carter.txt')

# book and freq dist
f = FreqDist(text1) # Moby Dick
print(f.most_common(10))

c = FreqDist(carter)
print(c.most_common(10))

# cumulative distribution of the words (by all presidents)
