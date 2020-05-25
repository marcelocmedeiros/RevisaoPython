# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
print('='*30)
print('{:*^30}'.format(' Pares Entre 1 e 50 '))
print('='*30)
print()

for c in range(2, 51, 2):
    print(c, end=', ')
print('S')
