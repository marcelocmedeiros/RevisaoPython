# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 14 LAÇO DE REPETIÇÃO WHILE ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia um número "N" inteiro qualquer
e mostre na tela os N primeiros elementos de uma sequência de Fibonacci
'''
print('='*30)
print('{:*^30}'.format(' Sequência de Fibonacci '))
print('='*30)
print()

# variável número de termos que quer exibir
num = int(input('Quantos termos você quer mostrar: '))
# 1° e 2° são predeterminados na sequência de Fibonacci
termo_1 = 0
termo_2 = 1
print(f'{termo_1} -> {termo_2}', end='')

# contador começa 3 pq o 1° e 2° são predeterminados
cont = 3

# um loop de num termos
while cont <= num:
    termo_3 = termo_1 +termo_2
    print(f' -> {termo_3}', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    cont += 1
print(' -> Fim')