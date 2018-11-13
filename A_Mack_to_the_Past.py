from random import *
import os

def embaralharPergunta (listaResposta):
    listaPergunta = []
    while (len(listaPergunta) < len(listaResposta)):
        temp = randint(0,len(listaResposta)-1)
        if listaResposta[temp] not in listaPergunta:
            listaPergunta.append(listaResposta[temp])
    return listaPergunta

def exibirParagrafos(lista):
    print()
    for x in range(len(lista)):
        print(lista[x],'\n')

def exibirListaNumerada(lista):
    print()
    for x in range(len(lista)):
        print(x+1,'-',lista[x],'\n')

def clearScreen():
    print('''\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n''')
    '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    '''

def validarSN():
    escolha = input('S/n: ').lower()
    while escolha != 's' and escolha != 'sim' and escolha != '' and escolha != 'n' and escolha != 'nao' and escolha != 'não':
        escolha = input('Escolha inválida\nS/n: ')
    if escolha == 's' or escolha == 'sim' or escolha == '':
        return False
    else:
        return True

def validarProsseguir():
    input('Pressione ENTER para prosseguir')

resposta1 = ['primeiro','segundo','terceiro','quarto','quinto','sexto']
pergunta1 = embaralharPergunta(resposta1)

def main():
    exibirParagrafos(resposta1)
    validarProsseguir()
    clearScreen()
    exibirListaNumerada(pergunta1)

main()