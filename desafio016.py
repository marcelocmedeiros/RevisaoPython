# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 08 GUSTAVO GUANABARA

'''
Faça um programa que leia um número real qualqeur e mostre na tela a sua porção inteira 
'''
print('='*30)
print('{:@^30}'.format('  PROÇÃO INTEIRA  '))
print('='*30)
print()

from math import trunc

num = float(input('Infome o número qualquer:'))

print()
print('O valor {} informado tem sua foram inteira {}'.format(num, trunc(num)))
