# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 09 GUSTAVO GUANABARA

'''
Faça um programa leia oum número de 0 a 9999 e moste cada um dos digitos separados.
ex: 1834
milhar:1; centena:8; dezena:3; unidade:4.
'''
print('='*30)
print('{:@^30}'.format('  STRAING DE NÚMEROS  '))
print('='*30)
print()

num =  int(input('Informe um número entre 0 e 9999:'))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print()
print('Analizando o número informado...')
print('Unidades:', u)
print('Dezenas:', d)
print('Centenas:', c)
print('Milhar:', m)
print()
