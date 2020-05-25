# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 12 CONDIÇÕES ANINHADAS ---> GUSTAVO GUANABARA

'''
Faça um Programa que faça o computador jogar Jokenpô com você.
'''
print('='*30)
print('{:+^30}'.format(' JOGO JOKENPÔ '))
print('='*30)
print()

# importar randint para sortear um item (0,2)
from random import randint
# importar sleep para dar uma pausa
from time import sleep

# variável item a ser sorteados
itens = ('pedra', 'papel', 'tesoura')
# jogada do computador
computador = randint(0,2)
print('''SUAS OPÇÕES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada: '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('-='*12)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*12)
sleep(1)
# condições para vencedor
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('PC VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:
    if jogador == 0:
        print('PC VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('PC VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')
