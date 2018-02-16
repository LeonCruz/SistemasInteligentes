"""Código para resolução do jogo "Ponte Escura". """

from random import choice, randint

def alterarTempo(p1, p2=0):
    global tempo_lamp

    if p1 > p2:
        tempo_lamp -= p1
    else:
        tempo_lamp -= p2

def quantEscolha(lista):
    global tempo_lamp
    global lado_A
    global lado_B
    global num_escolhas

    if len(lista) == 1:
        num_escolhas = 1
    else:
        num_escolhas =  randint(1, 2)

def moverPersonagemLadoA():
    print('\tLado A')

    quantEscolha(lado_A)

    print('Número de escolhas: ', num_escolhas)
    if num_escolhas == 1:
        p1 = choice(lado_A)
        lado_A.remove(p1)
        print('Personagem escolhido: ', p1)
        lado_B.append(p1)
        alterarTempo(p1)
    else:
        p1 = choice(lado_A)
        lado_A.remove(p1)
        p2 = choice(lado_A)
        lado_A.remove(p2)
        print('Personagens escolhidos: ', p1, ' e ', p2)
        lado_B.append(p1)
        lado_B.append(p2)
        alterarTempo(p1, p2)

    print('Esse o lado A: ', lado_A)
    print('Esse o lado B: ', lado_B)


def moverPersonagemLadoB():
    print('\tLado B')

    quantEscolha(lado_B)

    print('Número de escolhas: ', num_escolhas)
    if num_escolhas == 1:
        p1 = choice(lado_B)
        lado_B.remove(p1)
        lado_A.append(p1)
        alterarTempo(p1)
        print('Personagem escolhido: ', p1)
    else:
        p1 = choice(lado_B)
        lado_B.remove(p1)
        p2 = choice(lado_B)
        lado_B.remove(p2)
        print('Personagens escolhidos: ', p1, ' e ', p2)
        lado_A.append(p1)
        lado_A.append(p2)
        alterarTempo(p1, p2)

    print('Esse o lado A: ', lado_A)
    print('Esse o lado B: ', lado_B)


tempo_lamp = 30  # Tempo da lâmpada
lado_A = [1, 3, 6, 8, 12]  # Lado onde estão as pesssoas
lado_B = []  # Lado para onde as pesoas vão
num_escolhas = 0  # Número de personagens para a travessia

while tempo_lamp > 0:
    print('Tempo: ', tempo_lamp)
    moverPersonagemLadoA()
    print('Tempo: ', tempo_lamp)
    moverPersonagemLadoB()
