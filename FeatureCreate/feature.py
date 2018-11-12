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
