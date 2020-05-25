# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 09 GUSTAVO GUANABARA

'''
Faça um programa leia o nome completode uma pessoa e mostre:
1- O nome com todas as letras maipusculas e minúsculas
2- Quantas letras ao todo(sem considerar espaços)
3- Quantas letras tem o primeiro nome
'''
print('='*30)
print('{:@^30}'.format('  STRAING  '))
print('='*30)
print()

nome = str(input('Informe seu nome completo:'))

separado = nome.split()

print()
print('Seu nome em maiúsculas:',nome.upper())
print('Seu nome em minúsculas:',nome.lower())
print('O número de letras do nome sem espaços:',len(nome)-nome.count(' '))
print('O número de letras do 1° nome:',len(separado[0]))
print()
