
import csv
import nltk #Natural Language Processing
import re #Python's regular expression
from nltk.tokenize import word_tokenize 
from string import punctuation 
from nltk.corpus import stopwords
from more_itertools import unique_everseen
import emoji


# with open('teste.csv', mode='w', encoding='utf-8', newline='') as csvfile:
#     writeCSV = csv.writer(csvfile)
#     i = 0
#     while (i < 5):
#         writeCSV.writerow(['bolsonaro vagabundo'])
#         i = i + 1
#     writeCSV.writerow(['bolsonaro pilantra'])
#     writeCSV.writerow(['bolsonaro miliciano'])
#     writeCSV.writerow(['bolsonaro homofobico'])
#     writeCSV.writerow(['bolsonaro machista'])
#     writeCSV.writerow(['bolsonaro racista'])
#     writeCSV.writerow(['bolsonaro fascista'])
            



tweets = []
all_words = []
tweet = []
i = 0
print('lendo\n')
with open('bolsonaro_treino2.csv', mode='r', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        tweets.append(row[0])
        tweet = word_tokenize(row[0])
        for word in tweet:
            all_words.append(word)

def extract_features(tweet):
    tweet_words=set(tweet)
    features={}
    for word in word_features:
        features['contains(%s)' % word]=(word in tweet_words)
    return features 

print('montando palavras')
wordlist = nltk.FreqDist(all_words)
word_features = wordlist.keys()

print('treinando')
trainingFeatures=nltk.classify.apply_features(extract_features,tweets)

print(trainingFeatures)

NBayesClassifier=nltk.NaiveBayesClassifier.train(trainingFeatures)

print('label')

NBResultLabels = [NBayesClassifier.classify(extract_features(tweet[0])) for tweet in tweets]


print('analisando resultado')
if NBResultLabels.count('positive') > NBResultLabels.count('negative'):
    print("Overall Positive Sentiment")
    print("Positive Sentiment Percentage = " + str(100*NBResultLabels.count('positive')/len(NBResultLabels)) + "%")
else: 
    print("Overall Negative Sentiment")
    print("Negative Sentiment Percentage = " + str(100*NBResultLabels.count('negative')/len(NBResultLabels)) + "%")
