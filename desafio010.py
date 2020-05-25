# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 07 GUSTAVO GUANABARA
'''
Faça um programa que leia quanto dinheiro uma pessoa tem e mostre  o valor em dolares.
Considerando o dolar U$ 1.00 ==  R$4.50

'''
print('='*30)
print('{:$^30}'.format('  DOLARES  '))
print('='*30)

valor = float(input('Qual valor em Real deseja converter em Dolar:'))

dolar = valor / 4.50

print('Você informou R$ {:.2f} reais que no valor do câmbio de hoje é U$ {:.2f} dolares'.format(valor, dolar))

print('Você informou R$ {:.2f} reais que no valor do câmbio de hoje é U$ {:.2f} dolares'.format(valor, valor/4.50))