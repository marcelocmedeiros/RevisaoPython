# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 14 LAÇO DE REPETIÇÃO WHILE ---> GUSTAVO GUANABARA

'''
Faça um Programa que faça o computador pensar em um número inteiro entre 0 e 10.
Só que agora o jogador vai tentar advinhar até acertar, mostrando no final a quantos palpites foram necessários para vencer
'''
print('='*30)
print('{:*^30}'.format(' JOGO DA ADVINHAÇÃO 2 '))
print('='*30)
print()

# Para PC pensar vamos sortear entre 0-10 pela função randint
from random import randint
computador = randint(0,10)

print('Será que você consegue advinhar...')
# contador de tentativas
acertou = False
palpites = 0

# loop infinito até jogador = computador
while not acertou:
    # variável número entre 0 e 10
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente outra vez!')
        elif jogador > computador:
            print('Menos... Tente outra vez!')
print(f'Acertou... Você teve {palpites} tentativas. Parabéns!')
