from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import csv

def tratamento_dos_dados(dados):
    dados_tratados = []
    for dado in dados:
        dado = dado.split('    ')
        dados_tratados.append(dado)

    return dados_tratados

def obter_dados_das_fontes():
    dados = []
    print('lendo arquivo e fazendo preprocessamento\n')
    with open('bolsonaro_colocar_sentimento.csv', encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            dados.append(row[0])
    print('preprocessamento terminado')

    return dados

def pre_processamento():
    dados = obter_dados_das_fontes()
    dados_tratados = tratamento_dos_dados(dados)

    return dividir_dados_para_treino_e_validacao(dados_tratados)

def dividir_dados_para_treino_e_validacao(dados):
    quantidade_total = len(dados)
    percentual_para_treino = 0.75
    treino = []
    validacao = []

    for indice in range(0, quantidade_total):
        if indice < quantidade_total * percentual_para_treino:
            treino.append(dados[indice])
        else:
            validacao.append(dados[indice])

    return treino, validacao

train_set, test_set = pre_processamento()

cl = NaiveBayesClassifier(train_set)
accuracy = cl.accuracy(test_set)

frase = 'Bolsonaro eu te amo'

blob = TextBlob(frase,classifier=cl)

print('Esta frase é de caráter:{}'.format(blob.classify()))
print('Precisão da previsão:{}'.format(accuracy))