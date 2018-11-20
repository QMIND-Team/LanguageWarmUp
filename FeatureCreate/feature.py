'''
You will start with:
Tokenized, cleaned, phrases
Here, as the `phrases` variable.  Give it a look!
You will want to end up with:
Normallized vectors, ready to be passed into a neural net
'''
import random

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

with open("words.txt") as f:
    words = f.readlines()
words = [x.strip() for x in words]

phrases = []
for i in range (0,10):
    phraselength = random.randint(5,15)
    phrase = []
    for j in range(0,phraselength):
        choice = random.randint(0,len(words))
        phrase.append(words[choice])
        sentence = ' '.join(phrase)
    phrases.append(sentence)

print(phrases)

'''
Some ideas:
Let's use Bag of Words
Are there any libraries that have this built in?  (Almost certainly yes!)
How do I give those functions my data (Probably a Pandas Dataframe!)
'''
#wasn't working properly without lowercase set to false, I thint it has to do with apostrophes
#binary set to false will give us a count of how many times that word was present in the sentence

vectorizer = CountVectorizer(binary=True, lowercase=False, ngram_range=(2, 2))
vector = vectorizer.fit_transform(phrases)

print( vector.todense() )
print( vectorizer.vocabulary_ )
print(len(vectorizer.vocabulary_))

