# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 08 GUSTAVO GUANABARA

'''
Faça um programa que leia umm ângulo qualquer e mostre o valor do seu seno, cosseno e tangente.
'''
print('='*30)
print('{:*^30}'.format('  SENO COSSENO TANGENTE  '))
print('='*30)
print()

import math

angulo = float(input('Informe qualquer ângulo:'))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print()
print('O ângulo informado foi {:.0f}\nO seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))
print()

