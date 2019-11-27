import time
import tweepy
import re
import csv
from textblob import TextBlob
from translate import Translator
#from googletrans import Translator

def sentiment_analiser(tweet):
    #translator = Translator(to_lang="en")
    #print(tweet)
    #en_tweet = translator.translate(tweet)
    # print(tweet.text)
    # en_tweet = TextBlob(en_tweet.text)

    translator= Translator(from_lang="pt", to_lang="en")
    en_tweet = translator.translate(tweet)
    en_tweet = TextBlob(en_tweet)


    if en_tweet.polarity > 0:
        sentimento = '1'
    elif en_tweet.polarity < 0:
        sentimento = '0'
    else:
        sentimento = '0.5'

    return tweet + '\t' + sentimento
    

tweets = []
print('lendo arquivo e fazendo preprocessamento\n')
with open('bolsonaro_colocar_sentimento2.csv', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile)
    i = 0
    for row in readCSV:
        if i % 400 == 0 and i != 0:
            time.sleep(30)
        aux = ' '.join(row)
        #translator = Translator()
        #en_tweet = translator.translate(aux, dest='en')
        tweet_com_sentimento = sentiment_analiser(aux)
        tweets.append(tweet_com_sentimento)
        print(i)
        i = i + 1
print('preprocessamento terminado')


print('escrevendo treino\n')
with open('bolsonaro_colocar_sentimento21.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    writeCSV = csv.writer(csvfile)
    i = 0
    while (i < len(tweets)):
        writeCSV.writerow([tweets[i]])
        i = i + 1
print('treino escrito\n')


# tweet = 'Eu te amo'
# translator = Translator()
# print(tweet)
# en_tweet = translator.translate(tweet, dest='en')
# print(en_tweet.text)

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

