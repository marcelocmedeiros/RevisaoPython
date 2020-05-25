# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 08 GUSTAVO GUANABARA

'''
Faça um programa que leia comprimento do cateto oposto e o cateto adjacente de um triângulo retângulo. 
calcule e mostre o comprimento da hipotenusa
'''
print('='*30)
print('{:@^30}'.format('  COMPRIMENTO DA HIPOTENUSA  '))
print('='*30)
print()

from math import hypot

oposto = float(input('Informe o catetos oposto:'))
adjacente = float(input('Informe o catetos adjacente:'))

print()
print('O cateto oposto é {}\nO cateto adjacente é {}\nAssim o valor da hipotenusa é {}'.format(oposto, adjacente, hypot(oposto, adjacente)))
print()

