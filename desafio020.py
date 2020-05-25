# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 08 GUSTAVO GUANABARA

'''
Faça um programa que leia os quatro alunos e mostre a ordem sorteada.
'''
print('='*30)
print('{:#^30}'.format('  ORDEM SORTEADA  '))
print('='*30)
print()

from random import shuffle

aluno1 = str(input('Nome:'))
aluno2 = str(input('Nome:'))
aluno3 = str(input('Nome:'))
aluno4 = str(input('Nome:'))

lista = [aluno1, aluno2, aluno3, aluno4]

#shuffle embaralhe a sequência/lista não-vazia
shuffle(lista)

print()
print('A ordem dos aulos sorteados foi...\n{}'.format(lista))
print()
