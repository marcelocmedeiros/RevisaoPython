# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 12 CONDIÇÕES ANINHADAS ---> GUSTAVO GUANABARA

'''
Faça um Programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa. O salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode excerder 30% do salário ou então o empréstimo será negado.
'''
print('='*30)
print('{:+^30}'.format('Empréstimo Bancário/Casa Própria'))
print('='*30)
print()

valor =float(input('Informe o valor da casa: '))
salario =float(input('Informe oo seu salário: '))
anos =int(input('Informe em quantos anos vai pagar: '))

tempo  = anos * 12
prestacao = valor / tempo
maximo = salario * 0.3
print()
if prestacao <= maximo:
    print('Seu empréstimo foi aprovado!\nSua prestação será de R$ %.2f.'%prestacao)
else:
    print('Seu emprétimo não foi aprovado!\nVocê só pode comprometer até R$ %.2f\nA prestação da casa ficou em R$ %.2f este valor é maior do que você pode pagar'%(maximo, prestacao))
print()
