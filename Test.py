import pandas as pd
import numpy as np
import string
import re
import nltk
from autocorrect import spell

# Each column in the dataframe is determined by separating each line of text where there is a tab (\t).
yelpDataset = pd.read_csv('Yelp.txt', sep='\t', header=None, encoding='latin-1')

# The columns are named from left to right
yelpDataset.columns = ['review', 'sentiment']

# stopword is defined as a list of words like 'the', 'and', 'with', and are found in the nltk corpus.
stopword = nltk.corpus.stopwords.words('english')

# We removed the word 'not', as it may prove useful to include it for context later
stopword = [word for word in stopword if word != 'not']

# This is a lemmatizer function. It takes words like 'grew', 'grows' and 'grown' and 
# reduces them to their root word 'grow'
lm = nltk.WordNetLemmatizer()

#This function splits each word of a sentence if it has one or more non-letter characters
def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens

# This function removes all characters that aren't letters
def onlyAlpha(tokenizedList):
    text = [word for word in tokenizedList if word.isalpha()]
    return text

#This function uses the stopwords referenced earlier, and removes any instances of them
def noStop(tokenizedList):
    text = [word for word in tokenizedList if word not in stopword]
    return text

# This function spellchecks all words in the data
def spellCheck(tokenizedList):
    text = [spell(word) for word in tokenizedList]
    return text

# This function uses the lemmatizer referenced earlier on each word in a tokenized string
def lemmatize(tokenizedList):
    text = [lm.lemmatize(word) for word in tokenizedList]
    return text

def posTag(tokenizedList):
    text = nltk.pos_tag(tokenizedList)
    return text

#def posTagFix(tags):
    #sentence = ''
    #for item in tags:       
     #   for word in item:    
      #      sentence = sentence + (word[1] + "X" + word[0] if len(word[1]) == 2 else word[1] + word[0]) + " "
#    return sentence



yelpDataset['review_tokens'] = yelpDataset['review'].apply(lambda x: tokenize(x.lower()))
yelpDataset['review_alpha'] = yelpDataset['review_tokens'].apply(lambda x: onlyAlpha(x))
yelpDataset['review_nostops'] = yelpDataset['review_alpha'].apply(lambda x: noStop(x))
yelpDataset['review_spellCheck'] = yelpDataset['review_nostops'].apply(lambda x: spellCheck(x))
yelpDataset['review_lemmatized'] = yelpDataset['review_spellCheck'].apply(lambda x: lemmatize(x))
yelpDataset['review_posTag'] = yelpDataset['review_lemmatized'].apply(lambda x: posTag(x))
#yelpDataset['review_posTagFix'] = yelpDataset['review_posTag'].apply(lambda x: posTagFix(x))

df1 = pd.DataFrame(data = yelpDataset['review_posTag'])
#creates a list that can be vectorized later
df1 = df1['review_posTag'].tolist()
df2 = pd.DataFrame(data = yelpDataset['sentiment'])
df2 = df2['sentiment'].tolist()
print (df1[:5])