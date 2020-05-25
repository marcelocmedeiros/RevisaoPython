# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 09 GUSTAVO GUANABARA

'''
Faça um programa leia o nome completo de uma pessoa, no final mostre: o primeiro e o último nome
ex: maria dos santos saída maria santos
'''
print('='*30)
print('{:*^30}'.format('  FRASE '))
print('='*30)
print()

nome  = str(input('Informe seu nome completo: '))

separa = nome.split()

print()
print('Seu primeiro nome é {}\nSeu último nome é {}'.format(separa[0], separa[-1]))
print()
