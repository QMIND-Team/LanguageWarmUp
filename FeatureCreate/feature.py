'''
You will start with:
Tokenized, cleaned, phrases
Here, as the `phrases` variable.  Give it a look!
You will want to end up with:
Normallized vectors, ready to be passed into a neural net
'''
import random

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
    phrases.append(phrase)

print(phrases)





'''
Some ideas:
Let's use Bag of Words
Are there any libraries that have this built in?  (Almost certainly yes!)
How do I give those functions my data (Probably a Pandas Dataframe!)
'''
