# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 07 GUSTAVO GUANABARA

'''
Faça um programa que leia o peçode um produto e e mostre seu novo preço, com 5% de desconto
'''
print('='*30)
print('{:$^30}'.format('  DESCONTO 5%  '))
print('='*30)

preco = float(input('Informe o preço do produto:'))

desconto = preco - (preco*0.05)
print()
print('O produto que vocẽ escolheu é no valor de R$ {:.2f}\nMas com nosso desconto de 5% ele ficou por R$ {:.2f}.'.format(preco, desconto))
print()
