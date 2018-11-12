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