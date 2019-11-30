import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

dataset = pd.read_csv('tweets-mg.csv')
dataset.count()

dataset = pd.read_csv('c.csv')
tweets = []
classes = []
for text,sentiment in dataset.values:
    tweets.append[text]
    classes.append[sentiment]

vectorizer = CountVectorizer(analyzer="word")
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()

testes = ['Esse governo está no início, vamos ver o que vai dar',
         'Estou muito feliz com o governo de Minas esse ano',
         'O estado de Minas Gerais decretou calamidade financeira!!!',
         'A segurança desse país está deixando a desejar',
         'O governador de Minas é do PT']

freq_testes = vectorizer.transform(testes)
print(modelo.predict(freq_testes))

testes = ['bolsonaro deu show',
         'bolsonaro realiza um discurso cheio de ódio',
         'eu nao aguento mais o bolsonaro que homem escroto meu deus',
         'bolsonaro foi bem',
         'estamos orgulhosos do presidente']

freq_testes = vectorizer.transform(testes)
print(modelo.predict(freq_testes))