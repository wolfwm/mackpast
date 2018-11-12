from random import *

def embaralharPergunta (listaResposta):
    listaPergunta = []
    while (len(listaPergunta) < len(listaResposta)):
        temp = randint(0,len(listaResposta)-1)
        if listaResposta[temp] not in listaPergunta:
            listaPergunta.append(listaResposta[temp])
    return listaPergunta

resposta1 = ['primeiro','segundo','terceiro','quarto','quinto','sexto']
pergunta1 = embaralharPergunta(resposta1)

print(pergunta1)