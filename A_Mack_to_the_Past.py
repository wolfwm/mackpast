from random import *
#import os

def embaralharPergunta (listaParagrafos):
    listaPergunta = []
    while (len(listaPergunta) < len(listaParagrafos)):
        temp = randint(0,len(listaParagrafos)-1)
        if listaParagrafos[temp] not in listaPergunta:
            listaPergunta.append(listaParagrafos[temp])
    return listaPergunta

def exibirParagrafos(lista):
    print()
    for x in range(len(lista)):
        print(lista[x],'\n')
    validarProsseguir()

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
        return True
    else:
        return False

def validarProsseguir():
    input('Pressione ENTER para prosseguir')
    clearScreen()

def checkIfInRangeAndInListFromList(listToIndex, index, targetList):
        try:
            if int(index)-1 >= 0:
                if int(index)-1 < len(listToIndex):
                    if listToIndex[int(index)-1] in targetList:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return True
        except:
            return True

def pergConferirResp(listaParagrafos):
    listaPergunta = embaralharPergunta(listaParagrafos)
    flag = True
    while flag:
        clearScreen()
        listaResposta = []
        exibirListaNumerada(listaPergunta)
        for x in range(len(listaParagrafos)):
            print('Parágrafo',x+1,':')
            temp = input()
            while checkIfInRangeAndInListFromList(listaPergunta,temp,listaResposta):
                print('Escolha inválida\nParágrafo', x + 1, ':')
                temp = input()
            listaResposta.append(listaPergunta[int(temp)-1])
        if listaResposta == listaParagrafos:
            print('\nAcertou!\n')
            flag = False
            validarProsseguir()
        else:
            print('Errou')
            validarProsseguir()

def main():
    clearScreen()

    paragrafos1 = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto']

    exibirParagrafos(paragrafos1)

    pergConferirResp(paragrafos1)

main()