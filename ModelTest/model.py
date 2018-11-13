'''
You will start with:
Normallized vectors, sparse, representing phrases
Here as the `features` variable.  Give it a look!
You will want to end up with:
A trained model that predicts positive or negative sentiment!
(Woot!)

'''
import random

NUM_UNIQUE = 50

features = []
for i in range(20):
    piece = [0] * NUM_UNIQUE
    normal = 1.0
    while (normal > 0):
        place = random.randint(0, NUM_UNIQUE-1)
        amount = random.random()/4
        if (amount > normal):
            amount = normal
        piece[place] = amount
        normal -= amount
    features.append(piece)

print(features)



'''
Ideas/Questions:
Do any libaries have NaiveBayesClassifier built in?  (This is a yes, so which one?)
How do we arrange the data to be sent into the model?  (Probably with a Pandas Dataframe!)
'''