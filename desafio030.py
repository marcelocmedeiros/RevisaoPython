# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 10 CONDIÇÕES GUSTAVO GUANABARA

'''
Faça um Programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
'''
print('='*30)
print('{:#^30}'.format(' PAR ou IMPAR '))
print('='*30)
print()

num = int(input('Informe um número: '))
print()
#condição para ser par ou impar
if num % 2 == 0:
    print('Você informou %d e ele é número PAR!'%num)
else:
    print('Você informou %d e ele é número IMPAR!'%num)
print()