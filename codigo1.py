"""Código para a resolução do jogo "Ponte Escura"."""

# Importação das funções necessárias do Python
from random import choice, randint
from time import sleep, time

# Declaração das variáveis
tempo_lamp = 30  # Tempo da lâmpada
lado_A = [1, 3, 6, 8, 12]  # Lado onde estão as pesssoas
lado_B = []  # Lado para onde as pesoas vão
tentativas = 0 # Contador de tentativas até resolver
jogada = 0
tempo_decorrido = time() # Registra o tempo inicial
lista_movimentos = [] # Lista que irá armazenar os movimentos da máquina em cada rodada
movimento_rodadas = [] # Lista que irá armazenar os movimentos de todas as rodadas

"""Função anônima que salva em uma lista os movimentos da máquina."""
pegar_movimentos = lambda movimento: lista_movimentos.append(movimento)

"""Função anônima para testar se o movimento já foi feito."""
testar_movimento = lambda movimento: True if movimento in lista_movimentos else False

"""Função anônima para testar a quantidade de elementos do lado B."""
quantLadoB = lambda lado_B: True if len(lado_B) == 1 else False

def alterarTempo(p1, p2=0):
    """ Função que altera o tempo baseando-se no personagem
        de maior custo."""
    global tempo_lamp

    if p1 > p2:
        tempo_lamp -= p1
    else:
        tempo_lamp -= p2

def quantEscolha(lado):
    """Função que escolhe aleatóriamente a quantidade de pessoas que irão
        atravessar a ponte em uma jogada."""
    if len(lado) == 1:
        num_escolhas = 1
    else:
        num_escolhas =  randint(1, 2)

    return num_escolhas

def moverPersonagem(lado_sai, lado_entra):
    """Função que move os personagem pela ponte."""
    num_escolhas = quantEscolha(lado_sai)
    global jogada

    print('Número de escolhas: ', num_escolhas)
    
    if num_escolhas == 1:
        p1 = choice(lado_sai)

        if verificaUltimaJogada([p1]):
            print('----------Movimento Inválido----------')
            moverPersonagem(lado_sai, lado_entra)
		
        else:
            lado_sai.remove(p1)
            lado_entra.append(p1)
            print('Personagem escolhido: ', p1)

            alterarTempo(p1)
            pegar_movimentos([p1])
        
    else:
        p1 = choice(lado_sai)
        p2 = choice(lado_sai)
        while p2 == p1:
            p2 = choice(lado_sai)
			

        #if testar_movimento(sorted([p1, p2])):
            #moverPersonagem(lado_sai, lado_entra)
        if verificaUltimaJogada(sorted[p1, p2]):
            print('----------Movimento Inválido----------')
            moverPersonagem(lado_sai, lado_entra)
        else:
            lado_sai.remove(p1)
            lado_sai.remove(p2)
            lado_entra.append(p1)
            lado_entra.append(p2)
            print('Personagens escolhidos: ', p1, ' e ', p2)

            alterarTempo(p1, p2)

            pegar_movimentos(sorted([p1, p2]))
        
    jogada += 1
    return (sorted(lado_sai), sorted(lado_entra))

def reiniciarJogo():
    """Função que reinicia as variáveis quando a máquina perde."""
    global tempo_lamp
    global lado_A
    global lado_B
    global tentativas
    global movimento_rodadas
    global lista_movimentos
    global jogada

    tentativas += 1
    movimento_rodadas.append(lista_movimentos)
    lista_movimentos = []
    jogada = 0
    tempo_lamp = 30
    lado_A = [1, 3, 6, 8, 12]
    lado_B = []

def verificaUltimaJogada(movimento):
    global jogada
    global movimento_rodadas
	
    print(movimento_rodadas[last][jogada])
    print(movimento)

    if movimento_rodadas[len(movimento_rodadas)-1][jogada] == movimento:
        return True
    else:
        return False
	
	
# Laço onde o jogo irá ocorrer
while True:
    
    if lado_A != [] and tempo_lamp > 0:
        print('Tempo: ', tempo_lamp)

        print('----------Lado A----------')
        lado_A, lado_B = moverPersonagem(lado_A, lado_B)
        print('Lado A: {}\nLado B: {}'.format(lado_A, lado_B))

        sleep(1)

        print('Tempo: ', tempo_lamp)

        print('----------Lado B----------')
        lado_B, lado_A = moverPersonagem(lado_B, lado_A)
        print('Lado A: {}\nLado B: {}'.format(lado_A, lado_B))

        sleep(1)
		

    if tempo_lamp <= 0:
        reiniciarJogo()
        print('-----------\nMovimentos feitos:', *movimento_rodadas, sep = '\n')
        print('-----------')
        print('----------Jogo Reiniciado!----------')
        print('Numero de tentativas: %d' % tentativas)


    if tempo_lamp >= 0 and lado_A == []:
        tempo_decorrido = time() - tempo_decorrido
        print('\n\n----------FIM DO JOGO!----------')
        print('Numero de tentativas: %d' % tentativas)
        print('O tempo decorrido foi de %.2f segundos' % tempo_decorrido)
        break
