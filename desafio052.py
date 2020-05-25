# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia um númro inteiro e diga se ele é ou não um número primo.
'''
print('='*30)
print('{:*^30}'.format(' Número Primo '))
print('='*30)
print()

num = int(input('Informe um número inteiro: '))

cont = 0 

for c in range(1, num+1):
    if num % c == 0:
        cont += 1
print()
print(f'Como o número {num} foi divisível {cont} vezes')
print()
if cont ==  2:
    print('Assim este número é PRIMO!')
else:
    print('Assim este número NÃO É PRIMO!')
print()
