# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 09 GUSTAVO GUANABARA

'''
Faça um programa leia um nome de uma pessoa e diga se tem "SILVA" no nome
'''
print('='*30)
print('{:*^30}'.format('  PROCURA SILVA '))
print('='*30)
print()

nome = str(input('Informe seu nome completo: ')).upper()

print()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))
print()
