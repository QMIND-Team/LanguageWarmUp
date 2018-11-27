import pandas as pd
import numpy as np
import string


yelpDataset = pd.read_csv('Yelp.txt', sep='\t', header=None, encoding='latin-1')
yelpDataset.columns = ['review', 'sentiment']


def removePunct(text):
    noPunct = ''.join([char for char in text if char not in string.punctuation])
    return noPunct

yelpDataset['review_clean'] = yelpDataset['review'].apply(lambda x: removePunct(x.lower()))

df1 = pd.DataFrame(data = yelpDataset['review_clean'])
#numpy array for review 
df1 = df1.values
df2 = pd.DataFrame(data = yelpDataset['sentiment'])
#numpy array for sentiment 
df2 = df2.values
