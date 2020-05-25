# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 08 GUSTAVO GUANABARA

'''
Faça um programa que um professor sortei um dos quatro alunos para apagar o quadro.
'''
print('='*30)
print('{:#^30}'.format('  SORTEIO  '))
print('='*30)
print()

import random 

aluno1 = str(input('Nome:'))
aluno2 = str(input('Nome:'))
aluno3 = str(input('Nome:'))
aluno4 = str(input('Nome:'))

lista = [aluno1, aluno2, aluno3, aluno4]

#choice retornar um elemento aleatório da sequência/lista não-vazia
sorteio = random.choice(lista)

print()
print('O aluno sorteado foi...\n{}'.format(sorteio))
print()
