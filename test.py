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

    # translator= Translator(from_lang="pt", to_lang="en")
    # en_tweet = translator.translate(tweet)
    # en_tweet = TextBlob(en_tweet)
    
    if tweet.find('esquerda') != -1 or tweet.find('esquerdopata') != -1 or tweet.find('esquerdista') != -1 or tweet.find('luladrao') != -1 or tweet.find('bolsomito') != -1 or tweet.find('globolixo') != -1 or tweet.find('mito') != -1 or tweet.find('capitao') != -1 or tweet.find('2022') != -1 or tweet.find('2026') != -1 or tweet.find('petista') != -1 or tweet.find('lula ta preso') != -1 or tweet.find('comunista') != -1 or tweet.find('deus abencoe')!= -1:
        sentimento = '1'
    elif tweet.find('bolsonaro tomar') != -1 or tweet.find('bolsominion') != -1 or tweet.find('gado') != -1!= -1 or tweet.find('cidadao de bem') != -1 or tweet.find('reaça') != -1 or tweet.find('laranja') != -1:
        sentimento = '0'
    else:
        return tweet
    return tweet + '    ' + sentimento

    
tweets = []
print('lendo arquivo e fazendo preprocessamento\n')
with open('b.csv', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile)
    i = 0
    for row in readCSV:
        aux = ' '.join(row)
        # aux = ' '.join(aux.split())
        if aux.find('    ') != -1:
            tweets.append(aux)
        # tweets.append(sentiment_analiser(aux))
        i = i + 1
print('preprocessamento terminado')

print('escrevendo treino\n')
with open('c.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    writeCSV = csv.writer(csvfile)
    i = 0
    while (i < len(tweets)):
        writeCSV.writerow([tweets[i]])
        i = i + 1
print('treino escrito\n')
