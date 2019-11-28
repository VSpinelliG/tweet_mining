import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

dataset = pd.read_csv('bolsonaro_colocar_sentimento3.csv')
tweets = []
classes = []
for text,sentiment in dataset.values:
    tweets.append[text]
    classes.append[sentiment]

vectorizer = CountVectorizer(analyzer="word")
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)