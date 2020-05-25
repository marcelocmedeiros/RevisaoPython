# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 16 Variáveis Composta Tuplas ---> GUSTAVO GUANABARA

'''
Faça um programa que gere 5 números aleatórios e coloque em uma tupla. Depois mostre 
alistagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
print('='*30)
print('{:*^30}'.format(' 5 Números Aleatórios '))
print('='*30)
print()

from random import randint

num = (randint(0, 50), randint(0, 50), randint(0, 50),randint(0, 50),randint(0, 50),randint(0, 50),)

print(f'Alistagem de números gerados foi: {num}')
print(f'Alistagem de números gerados em ordem é: {sorted(num)}')
print(f'Na listagem de números o menor será: {min(num)}')
print(f'Na listagem de números o maior será: {max(num)}')


