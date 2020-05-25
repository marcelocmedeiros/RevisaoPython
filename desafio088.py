# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 18 Variáveis Composta Listas 2° parte---> GUSTAVO GUANABARA

'''
Faça um programa que ajude um jogador da MEGA SENA criar palpites. O programa
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo. Cadastrando tudo em uma lista composta.
'''
print('='*30)
print('{:*^30}'.format(' MEGA SENA '))
print('='*30)
print()

# importar randint para sortaer números e sleep para dar pausa 
from random import randint
from time import sleep
# lista transitoria para cada sorteio
lista = list()
# lista pricipal onde fica todos os jogos
jogos = list()

# variável de quantidade de jogos p ser sorteados
quant = int(input(('Quantos jogos você quer que eu sortei: ')))
tot = 1
while tot <= quant:
    cont = 0
    # loop infinito para sortear até completar 6 n° sem repetição
    while True:
        num = randint(1, 60)
        # só add na lista se ainda não estiver se não sortear novamete
        if num not in lista:
            lista.append(num)
            cont += 1
        # para quando chegar a 6 n° diferentes pare
        if cont >= 6:
            break
    # coloca os n° sorteados em ordem crescente
    lista.sort()
    # vou add uma copia da lista[:] em jogos
    jogos.append(lista[:])
    # apago a lista para gerar nova lista
    lista.clear()
    # para não geral um loop infinito
    tot += 1
print('-=' * 3, f'SOTEANDO {quant} JOGOS', '-=' * 3)
# for para cada índice da lista i, l
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
