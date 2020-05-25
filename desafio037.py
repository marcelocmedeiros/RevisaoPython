# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 12 CONDIÇÕES ANINHADAS ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia um número inteiro qualquer e peça para o usuário escolher 
qual será a base de conversão:
    1- para binário
    2- para octal
    3- para hexadecimal
'''
print('='*30)
print('{:+^30}'.format(' PROGRAMA CONVERSOR DE BASES  '))
print('='*30)
print()

num =  int(input('Informe um número inteiro: '))
base = int(input('1- Para Binário\n2- Para Octal\n3- Para Hexadecimal\nEm qual base você quer converte o valor:'))
print()

if base == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida. Tente novamente!')
    print()
