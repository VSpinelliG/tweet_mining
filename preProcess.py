import nltk
import re
import csv
import emoji
from nltk.tokenize import word_tokenize
from string import punctuation 
from nltk.corpus import stopwords 
from more_itertools import unique_everseen

stopwords = set(stopwords.words('portuguese') + list(punctuation))

def load_dict_smileys():
    
    return {
        ":‑)":"smiley",
        ":-]":"smiley",
        ":-3":"smiley",
        ":->":"smiley",
        "8-)":"smiley",
        ":-}":"smiley",
        ":)":"smiley",
        ":]":"smiley",
        ":3":"smiley",
        ":>":"smiley",
        "8)":"smiley",
        ":}":"smiley",
        ":o)":"smiley",
        ":c)":"smiley",
        ":^)":"smiley",
        "=]":"smiley",
        "=)":"smiley",
        ":-))":"smiley",
        ":‑D":"smiley",
        "8‑D":"smiley",
        "x‑D":"smiley",
        "X‑D":"smiley",
        ":D":"smiley",
        "8D":"smiley",
        "xD":"smiley",
        "XD":"smiley",
        ":‑(":"sad",
        ":‑c":"sad",
        ":‑<":"sad",
        ":‑[":"sad",
        ":(":"sad",
        ":c":"sad",
        ":<":"sad",
        ":[":"sad",
        ":-||":"sad",
        ">:[":"sad",
        ":{":"sad",
        ":@":"sad",
        ">:(":"sad",
        ":'‑(":"sad",
        ":'(":"sad",
        ":‑P":"playful",
        "X‑P":"playful",
        "x‑p":"playful",
        ":‑p":"playful",
        ":‑Þ":"playful",
        ":‑þ":"playful",
        ":‑b":"playful",
        ":P":"playful",
        "XP":"playful",
        "xp":"playful",
        ":p":"playful",
        ":Þ":"playful",
        ":þ":"playful",
        ":b":"playful",
        "<3":"love"
        }

def processTweet(tweet):
    tweet = tweet.lower() # convert text to lower-case
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet) # remove URLs
    tweet = re.sub('@[^\s]+', '', tweet) # remove usernames
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet) # remove the # in #hashtag
    tweet = re.sub('kk+k*', '', tweet) # remove risada (kkk)
    
    SMILEY = load_dict_smileys()  
    words = tweet.split()
    reformed = [SMILEY[word] if word in SMILEY else word for word in words]
    tweet = " ".join(reformed)
    tweet = emoji.demojize(tweet)
    # tweet = tweet.replace(":"," ")
    tweet = re.sub(':[^\s]*:+', '', tweet) #remove emoji 
    
    tweet = ' '.join(tweet.split())
    tweet = word_tokenize(tweet)
    tweet = [word for word in tweet if word not in stopwords]
    new_tweet = ''
    for word in tweet:
        new_tweet = new_tweet + word + ' '
    return new_tweet

def removeDuplicates():
    with open('bolsonaro.csv','r', encoding="utf-8") as f, open('bolsonaro_cru.csv','w', encoding="utf-8") as out_file:
        out_file.writelines(unique_everseen(f))

#-----------------------------------------------

# tweets = []
# processedTweets = []

# print('lendo arquivo e fazendo preprocessamento\n')
# with open('bolsonaro_sem_repeticoes.csv', encoding='utf-8') as csvfile:
#     readCSV = csv.reader(csvfile)
#     # i = 0
#     for row in readCSV:
#         processedTweets = processTweet(row[0])
#         tweets.append(processedTweets)
#         # print('r: ',i)
#         # i = i + 1
# print('preprocessamento terminado')

# quantidade_total = len(tweets)
# qtd_treino = int(len(tweets) * 0.75)
# tweets_treino = []
# tweets_teste = []

# print('separando o arquivo para treino e teste')
# for indice in range(1, quantidade_total):
#     if indice < qtd_treino:
#         tweets_treino.append(tweets[indice])
#     else:
#         tweets_teste.append(tweets[indice])
# print('separação concluida')


# print('escrevendo treino\n')
# with open('bolsonaro_sem_repeticoes2.csv', mode='w', encoding='utf-8', newline='') as csvfile:
#     writeCSV = csv.writer(csvfile)
#     i = 0
#     while (i < len(tweets)):
#         writeCSV.writerow([tweets[i]])
#         # print('w: ',i)
#         i = i + 1
# print('treino escrito\n')

# print('escrevendo teste\n')
# with open('bolsonaro_teste2.csv', mode='w', encoding='utf-8', newline='') as csvfile:
#     writeCSV = csv.writer(csvfile)
#     i = 0
#     while (i < len(tweets_teste)):
#         writeCSV.writerow([tweets_teste[i], 'neutro'])
#         # print('w: ',i)
#         i = i + 1
# print('teste escrito\n')