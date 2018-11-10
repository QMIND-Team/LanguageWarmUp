# Twitter Sentiment Analysis

## What The Project Was

>The programmer worked on a sentiment analysis project, where they were interested in developing a sentiment analysis model to 
>analyze sentiment of tweets by people in different cities to see if there was a correlation between the number of positive tweets and city. In short, the programmer was interested in determining in which cities are the citizens happiest.

## Toolkits and Libraries Used for the Project

>The programmer used **BeautifulSoup**, **Pandas**, **NLTK**, **pprint**, **numpy**, **csv**, and **matplotlib.pyplot** libraries and toolkits.

## Datasets and Features Used for the Project

>The project made use of the _"Sentiment 140"_ data set that was created by _**Stanford University**_. A copy of the data set can be found [_here_](http://help.sentiment140.com/for-students/).
>The data set was a ranked data set that used the following fields for consideration in the sentiment analysis:

      0 - the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
      1 - the tweet id
      2 - the data of the tweet
      3 - the query
      4 - the user the tweet belongs to
      5 - the text of the tweet itself

>For training the sentiment analysis model, 1.6 million distinct entries were used for training, where half of the tweets were labelled as positive,
> and the other half of tweets were labelled negative. 
>Since the data set contained a few unrelated fields for the desired purpose of the project, the programmer decided to drop fields 1-4 as seen above. This
>left tweet polarity, and the text of the tweet itself as the main focus of the data set and model training.


## Data Preparation

>After determining which fields in the data set were relevant to the project, the programmer then proceeded to clean the data, since there were some 
>data entries that were obviously invalid (used a string length check to verify which data entries were within the 140 character limit typical of a tweet
>where it was found some entries exceeded the 140 character limit). Once that was completed, the programmer then took the HTML encoded text and parsed 
>it using **BeautifulSoup**.

>After parsing the text, the programmer then refined it to remove any twitter mentions, and links as they concluded that these would not add any value to the model. 
>The programmer then found UTF-8 encoded text which interfered with the text processing, so they used 'utf-8-sig' to decode the text and replace it with a'?'.

>Lastly, the programmer decided to remove any special characters contained in the tweet to account for hashtags since the special characters may interfere with
>the model processing.

>With cleaned data, the programmer then used the cleaning function that accounted for the above cleaning necessities to clean the whole data set. Once this was 
>completed, the programmer then exported the data to a csv file to use for training, where the data set was divided into four distinct batches.

