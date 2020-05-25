# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 09 GUSTAVO GUANABARA

'''
Faça um programa leia um nome de uma cidade e diga se ela começa ou não com nome "Santo"
'''
print('='*30)
print('{:*^30}'.format('  PROCURA  '))
print('='*30)
print()

'''nome = str(input('Informe o nome da cidade:')).upper()

separado = nome.split()

print(separado[0] == 'SANTO')'''

# outra alternativa
nome = str(input('Informe o nome da cidade:')).strip()

print(nome[:5].upper() == 'SANTO')
