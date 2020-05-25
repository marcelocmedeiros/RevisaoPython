# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 16 Variáveis Composta Tuplas ---> GUSTAVO GUANABARA

'''
Faça um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrálo por extenso.
'''
print('='*30)
print('{:*^30}'.format(' Número por Extenso '))
print('='*30)
print()

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatoze', 'quinze', 'deseseis',
        'desesete', 'dezoit', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    # só para de perguntar quando estive entre  (0 <= n <= 20)
    if 0 <= n <= 20:
        break
    print('{:*^30}'.format(' Tente novamente '))
print(f'Você digitou o número {num[n]}')
