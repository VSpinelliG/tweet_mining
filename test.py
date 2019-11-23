import tweepy
import re
import csv
from textblob import TextBlob
from googletrans import Translator

def sentiment_analiser(tweet):
    translator = Translator()
    print(tweet)
    tweet = translator.translate(tweet, dest='en')
    print(tweet.text)
    tweet = TextBlob(tweet.text)

    if tweet.polarity > 0:
        sentimento = '1'
    elif tweet.polarity < 0:
        sentimento = '0'
    else:
        sentimento = '0.5'

    return tweet + '\t' + sentimento
    

tweets = []
print('lendo arquivo e fazendo preprocessamento\n')
with open('bolsonaro_colocar_sentimento.csv', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        try:
            tweet_com_sentimento = sentiment_analiser(row[0])
        except Exception as e:
            print(str(e))
            continue
        tweets.append(tweet_com_sentimento)
print('preprocessamento terminado')

print('escrevendo treino\n')
with open('bolsonaro_com_sentimento.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    writeCSV = csv.writer(csvfile)
    i = 0
    while (i < len(tweets)):
        writeCSV.writerow([tweets[i]])
        i = i + 1
print('treino escrito\n')



# import csv
# import nltk #Natural Language Processing
# import re #Python's regular expression
# from nltk.tokenize import word_tokenize 
# from string import punctuation 
# from nltk.corpus import stopwords
# from more_itertools import unique_everseen
# import emoji        



# tweets = []
# all_words = []
# tweet = []
# i = 0
# print('lendo\n')
# with open('bolsonaro_treino2.csv', mode='r', encoding='utf-8') as csvfile:
#     readCSV = csv.reader(csvfile)
#     for row in readCSV:
#         tweets.append(row[0])
#         tweet = word_tokenize(row[0])
#         for word in tweet:
#             all_words.append(word)

# def extract_features(tweet):
#     tweet_words=set(tweet)
#     features={}
#     for word in word_features:
#         features['contains(%s)' % word]=(word in tweet_words)
#     return features 

# print('montando palavras')
# wordlist = nltk.FreqDist(all_words)
# word_features = wordlist.keys()

# print('treinando')
# trainingFeatures=nltk.classify.apply_features(extract_features,tweets)

# print(trainingFeatures)

# NBayesClassifier=nltk.NaiveBayesClassifier.train(trainingFeatures)

# print('label')

# NBResultLabels = [NBayesClassifier.classify(extract_features(tweet[0])) for tweet in tweets]


# print('analisando resultado')
# if NBResultLabels.count('positive') > NBResultLabels.count('negative'):
#     print("Overall Positive Sentiment")
#     print("Positive Sentiment Percentage = " + str(100*NBResultLabels.count('positive')/len(NBResultLabels)) + "%")
# else: 
#     print("Overall Negative Sentiment")
#     print("Negative Sentiment Percentage = " + str(100*NBResultLabels.count('negative')/len(NBResultLabels)) + "%")

