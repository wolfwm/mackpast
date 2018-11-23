from random import *
#import os

def telaInicio():
    clearScreen()
    print('''
                                        ___       __  ___           __      __           __  __            ____             __ 
                                       /   |     /  |/  /___ ______/ /__   / /_____     / /_/ /_  ___     / __ \____ ______/ /_
                                      / /| |    / /|_/ / __ `/ ___/ //_/  / __/ __ \   / __/ __ \/ _ \   / /_/ / __ `/ ___/ __/
                                     / ___ |   / /  / / /_/ / /__/ ,<    / /_/ /_/ /  / /_/ / / /  __/  / ____/ /_/ (__  ) /_  
                                    /_/  |_|  /_/  /_/\__,_/\___/_/|_|   \__/\____/   \__/_/ /_/\___/  /_/    \__,_/____/\__/  
                                                                                                                               
    \n\n\n
    \n\n\n\n\n\n\n\n\n\n
    Alunos: Wolfgang Walder, Kleber Yoshida, Jorge Gomes
    
    A História do Mackenzie
    
    Instruções para jogar:
    -Pressione ENTER para iniciar o jogo e avançar a cada nº inserido
    -Esse jogo da memória irá mostrar a estória em partes da Universidade Presbiteriana Mackenzie
    -Insira os parágrafos em ordem
    -Você terá 5 tentativas para acertar a ordem correta
    -A cada fase você será pontuado com 100, 120 ou 150 pontos, dependendo do nº de tentativas utilizadas
    -A cada tentativa errada, você perderá -100 pontos
    -Ao final do jogo você irá receber um título honorário dependendo da sua pontuação total
    ''')
    validarProsseguir()

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

'''
def validarSN():
    escolha = input('S/n: ').lower()
    while escolha != 's' and escolha != 'sim' and escolha != '' and escolha != 'n' and escolha != 'nao' and escolha != 'não':
        escolha = input('Escolha inválida\nS/n: ').lower()
    if escolha == 's' or escolha == 'sim' or escolha == '':
        return True
    else:
        return False
'''

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
    exibirParagrafos(listaParagrafos)
    pontos = 0
    flag = True
    while flag:
        listaPar = []
        for z in range(len(listaParagrafos)):
            listaPar.append(listaParagrafos[z])
        listaPergunta = embaralharPergunta(listaPar)
        for i in range(5):
            listaResposta = []
            exibirListaNumerada(listaPergunta)
            print('Tentativas extra:', 4 - i)
            for x in range(len(listaPar)):
                print('Parágrafo', x + 1,':')
                temp = input()
                while checkIfInRangeAndInListFromList(listaPergunta,temp,listaResposta):
                    print('Escolha inválida\nParágrafo', x + 1, ':')
                    temp = input()
                listaResposta.append(listaPergunta[int(temp)-1])
            if listaResposta == listaPar:
                print('\nAcertou!\n')
                flag = False
                if i == 0:
                    pontos += 150
                    print('Recebeu 150 pontos')
                elif i < 2:
                    pontos += 120
                    print('Recebeu 120 pontos')
                else:
                    pontos += 100
                    print('Recebeu 100 pontos')
                break
            else:
                print('Errou')
                j = 0
                while j < len(listaPar):
                    if listaResposta[j] == listaPar[j]:
                        for y in range(len(listaPergunta)):
                            if listaPergunta[y] == listaResposta[j]:
                                del listaPergunta[y]
                                break
                        del listaResposta[j]
                        del listaPar[j]
                    else:
                        j += 1
                if i == 4:
                    pontos -= 100
                    print('Perdeu 100 pontos')
                validarProsseguir()
    print('Saldo de pontos da fase:',pontos)
    validarProsseguir()
    return pontos

def fimDeJogo(pontos, paragrafos):
    parags = []
    for x in range(len(paragrafos)):
        for y in range(len(paragrafos[x])):
            parags.append(paragrafos[x][y])

    print('''
                                    ___       __    _      __    __       _              __         __  ___           __                    _    
                                   /   |     / /_  (_)____/ /___/_/ _____(_)___ _   ____/ /___     /  |/  /___ ______/ /_____  ____  ____  (_)__ 
                                  / /| |    / __ \/ / ___/ __/ __ \/ ___/ / __ `/  / __  / __ \   / /|_/ / __ `/ ___/ //_/ _ \/ __ \/_  / / / _ \
                                 / ___ |   / / / / (__  ) /_/ /_/ / /  / / /_/ /  / /_/ / /_/ /  / /  / / /_/ / /__/ ,< /  __/ / / / / /_/ /  __/
                                /_/  |_|  /_/ /_/_/____/\__/\____/_/  /_/\__,_/   \__,_/\____/  /_/  /_/\__,_/\___/_/|_|\___/_/ /_/ /___/_/\___/ 
                                
    ''')

    for i in range(len(parags)):
        print(parags[i], '\n')

    print('Pontuação final:', pontos)

    title = ''

    if pontos == 750:
        title = 'Reverendo Chamberlain'
    elif pontos >= 600:
        title = 'John Mackenzie'
    elif pontos >= 500:
        title = 'Mackenzista'
    else:
        title = 'Vestibulando'

    print('Seu titulo de honra é:',title)

def main():
    telaInicio()

    pontos = 0

    paragrafos = []

    paragrafos1 = \
        [
            '''                 O Instituto Presbiteriano Mackenzie iniciou suas atividades em 1869. Uma história que se mistura
            com a própria história da cidade de São Paulo e do Brasil.''',

            '''                 Com a vinda à cidade de São Paulo em 1970, o casal de missionários presbiterianos George
            Whitehill Chamberlain (1839-1902), Pastor da Igreja Presbiteriana de São Paulo, de 1869 a 1888, e Mary Chamberlain
            (1840-1930), educadora, foram os pioneiros na criação do que hoje conhecemos como Universidade Presbiteriana Mackenzie.
            Em 1870, enquanto o reverendo Chamberlain empreendia viagens missionárias pelo interior do Estado, sua esposa, Mary,
            dedicava-se à área pedagógica na residência do casal, na Rua Visconde de Congonhas do Campo, nº1, localizado entre
            os bairros Campos Elíseos e Bom Retiro.''',

            '''                 Na sala de visita da casa, três crianças, sendo dois meninos e uma menina, foram os primeiros
            alunos de um sistema educacional revolucionário no ensino brasileiro, em turmas mistas. Nascia, assim, uma escola
            socialmente responsável, integrada à sociedade e com estratégias pedagógicas inovadoras e da sua ostensiva prática
            de inclusão social, étnica e política.''',

            '''                 Em 1871, já contava com 44 alunos e teve que se mudar, pois a sala de estar do casal já não
            comportava mais tantos alunos. Foi então, que a Sra. Chamberlain mudou-se para um novo endereço na rua Nova São José,
            atual Libero Badaró. A partir daí foi fundada a Escola Americana, embrião do Colégio Presbiteriano Mackenzie.'''
        ]
    paragrafos.append(paragrafos1)

    paragrafos2 = \
        [
            '''                 A partir de 1872, as aulas passaram a ser pagas - 12 mil réis por trimestre - concedendo-se
            bolsas parciais e integrais para os alunos carentes.
            Na escola não havia discriminação, pois estudavam tanto filhos de escravos, como de famíliastradicionais, como
            os sobrenomes Campos Salles, Prudente de Moraes e Rangel Pestana, entre outros.''',

            '''                 Em 1875 a escola já contava com 500 alunos, e em 1876, houve uma nova mudança de endereço, agora
            para a esquina das ruas Ipiranga e São João, mais precisamente na Rua de São João, nº 139 a 187, (próximo ao Largo dos Curros,
            atual Praça da República). Foi considerado o primeiro prédio construído para fins educacionais e religiosos.''',

            '''                 Em 1878 a Escola Americana recebeu a visita do imperador D. Pedro II, acompanhado de grande comitiva,
            que se entusiasmava com a pedagogia americana, porém não podia ajudar financeiramente, pois o Brasil era um país católico
            e a escola americana era dirigida por um protestante.''',

            '''                 A partir de 1880, surgem as primeiras edificações, Edifício Sinclair (1881) e Edifício Couto de Magalhães
            (1885) e a inauguração dos primeiros cursos de nível superior: Filosofia (1886) e Comércio(1890). Foram construídos também
            um edifício cuja parte superior era reservada para o internato feminino, e o térreo para dois escritórios e três
            espaçosas salas de aula.'''
        ]
    paragrafos.append(paragrafos2)

    paragrafos3 = \
        [
            '''                 Com a expansão e novos alunos ingressados, adquiriu-se uma área de 27,7 mil metros quadrados no
            bairro de Higienópolis.''',

            '''                 A Escola Americana já era internacionalmente famosa, dessa forma o advogado norte-americano John Theron Mackenzie
            que, sem nunca ter vindo ao Brasil, interessou-se pela causa nobre da escola e fez constar em seu testamento, em 1890,
            uma doação à Igreja Presbiteriana norte-americana para que se construísse no Brasil uma escola de Engenharia.''',

            '''                 Desde os 12 anos de idade, John Theron Mackenzie lia nos jornais nova-iorquinos artigos em que o político
            brasileiro José Bonifácio de Andrade e Silva defendia a necessidade de se intensificar a instrução no Brasil. John tinha
            o desejo de estudar Magistério e mudar-se para o Brasil a fim de lecionar, por isso antes de sua morte doou para a
            Igreja Presbiteriana norte-americana a importância de US$ 30.000,00, acrescidos de outros US$ 20.000,00 doados pelas
            suas irmãs, para a construção no Brasil de uma Escola de Engenharia.''',

            '''                 E em 1895 o nome “PROTESTANT COLLEGE” é mudado para “MACKENZIE COLLEGE”, em homenagem a
            John Theron Mackenzie – o Benfeitor. E era plasmada por duas vertentes: a confessionalidade e a Pedagogia Americana.''',

            '''                 Em fevereiro de 1896, já em Higienópolis, era inaugurada a primeira Escola de Engenharia de caráter privado do país.'''
        ]
    paragrafos.append(paragrafos3)

    paragrafos4 = \
        [
            '''                 A vocação de pioneirismo ficou evidenciada na criação da primeira experiência oficial de cotitulação
            internacional, tendo a University of the State of New York como entidade associada (1893).''',

            '''                 No século XX, o Mackenzie deu origem ao primeiro curso de Química Industrial de São Paulo (1911),
            criou o mais antigo curso de Engenharia Química do país (1922), introduziu, de forma pioneira, o Sistema Decimal Dewey
            de catalogação de bibliotecas no país (1926) e produziu o primeiro curso de Biblioteconomia do Brasil (1930).''',

            '''                 Na década de 40, novos cursos foram introduzidos como a Faculdade de Filosofia, Ciências e Letras
            em 1946, Faculdade de Arquitetura, em 1947 (a primeira no estado de São Paulo) e a Faculdade de Ciências Econômicas, em 1950.''',

            '''                 Em 1952, o Mackenzie foi considerado de fato uma universidade com quatro escolas superiores: Escola de Engenharia,
            Faculdade de Arquitetura, Faculdade de Filosofia, Ciências e Letras (1946) e Faculdade de Ciências Econômicas (1950),
            época em que o país contava com menos de duas dezenas de universidades – no estado de São Paulo eram apenas duas.''',

            '''                 A Faculdade de Direito é inaugurada em 1953'''
        ]
    paragrafos.append(paragrafos4)

    paragrafos5 = \
        [
            '''                 Em 1965 o Mackenzie nomeou a Dra. Esther de Figueiredo Ferraz como reitora. Ela foi a primeira
            mulher a assumir um cargo de reitora em universidades brasileiras.''',

            '''                 Em 1970, percebendo e visando o crescimento dos setores tecnológicos no país, o Mackenzie abre
            a Faculdade de Tecnologia, no qual se tornaria em 1999 em Faculdade de Computação e Informática. Teve como sua diretora,
            Aurora Catharina Giora Albanese, que posteriormente se tornou Reitora da Universidade Presbiteriana Mackenzie (entre 1985 e 1997).''',

            '''                 O nome Universidade Presbiteriana Mackenzie foi adotada somente a partir de 1999.''',

            '''                 Cursos de pós-graduação foram implantados em 1975 (lato sensu) e em 2003 (stricto sensu).''',

            '''                 Atualmente, há cerca de 40 mil alunos em mais de 40 cursos nos diversos campus do Mackenzie. As
            unidades de São Paulo e Tamboré oferecem desde a educação infantil à pós-graduação. A unidade de Brasília atende ao
            colégio e à pós-graduação que também está presente em Campinas, Rio de Janeiro e Recife.'''
        ]
    paragrafos.append(paragrafos5)

    paragrafos6 = \
        [
            '''            Seus valores e princípios para o século XXI estão pautados em:
                    ·Na conduta pessoal: dignidade, caráter, integridade e espírito mackenzista;
                    ·No relacionamento interpessoal: lealdade, respeito mútuo, compreensão, honestidade e humildade;
                    ·No exercício da atividade profissional: ética, competência, criatividade, disciplina, dedicação e disposição para o trabalho voluntário;
                    ·No processo de decisão: busca de consenso, de justiça, de verdade, de igualdade de oportunidades para todos;''',

            '''            PECULIARIDADES INSTITUCIONAIS:
                    ·Liberdade de crença e de expressão
                    ·Aceitação das minorias étnicas, religiosas e políticas
                    ·Integração dos diversos segmentos sócio-econômicos
                    ·Orientação religiosa cristã e reformada, conhecida como “protestante”, com fundamento na Bíblia Sagrada
                    ·Aplicação da “pedagogia americana”
                    ·Magistério feminino
                    ·Classes mistas
                    ·Educação Física para ambos os sexos
                    ·Eliminação dos castigos físicos
                    ·Experimentação como estratégia de ensino
                    ·Método Intuitivo: “Lições de coisas” (as coisas antes das palavras)
                    ·O Mackenzie foi pioneiro em receber filhos de abolicionistas, republicanos, protestantes  e judeus
                    ·Como nem todos dispunham de recursos para pagar, instituiu-se o sistema de bolsa de estudos em 1872.''',

            '''            MISSÃO DO MACKENZIE PARA O SÉCULO XXI
            “Educar o ser humano criado à imagem de Deus, para o exercício consciente e crítico da cidadania e da dignidade,
            preparando-o para a vida, contribuindo, assim, para o desenvolvimento do ser e da sociedade, por meio do ensino e
            das atividades científicas, culturais, esportivas, sociais, éticas e espirituais.”''',

            '''            VISÃO DO MACKENZIE PARA SÉCULO XXI
            “O Mackenzie, como instituição presbiteriana, dedica-se às ciências divinas e humanas; caracteriza-se pela busca
            contínua da excelência no ensino e na pesquisa; prima pela formação integral do ser humano, em ambiente de fé cristã
            evangélica reformada.”'''
        ]
    paragrafos.append(paragrafos6)

    pontos += pergConferirResp(paragrafos1)

    pontos += pergConferirResp(paragrafos2)

    pontos += pergConferirResp(paragrafos3)

    pontos += pergConferirResp(paragrafos4)

    pontos += pergConferirResp(paragrafos5)

    fimDeJogo(pontos, paragrafos)

main()