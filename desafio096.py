# Marcelo Campos de Medeiros
# ADS UNIFIP
# Lista_2_de_exercicios
# 15/03/2020

'''
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

# variáveis
num_1 = int(input('Informe o primeiro número? '))
num_2 = int(input('Informe o segundo número? '))
num_3 = int(input('Informe o terceiro número? '))

# mostrando os 1ª, 2ª e 3ª números em ordem decrescente

if num_1 == num_2 == num_3:
    print(f'{num_1}, {num_2} e {num_3}')
else:
    if num_1 < num_2 < num_3:
        print(f'{num_3}, {num_2} e {num_1}')
    elif num_1 < num_3 and num_3 > num_2:
      