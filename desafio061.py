# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 14 LAÇO DE REPETIÇÃO WHILE ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o primeiro termo e a razão de uma P.A.
Mostrando os 10 primeiros termos da progressão usando while.
'''
print('='*30)
print('{:*^30}'.format(' P.A. NO WHILE '))
print('='*30)
print()

# variáveis 1° termo e razão da P.A. / termo
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da P.A.: '))

# contador
termo = primeiro
cont = 1

# loop de 1 até 10
while cont <= 10:
    # lembrando o end= '' serve para juntar os dois prints
    print(f'{termo} ->', end='')
    termo += razão
    cont += 1
print(' fim')
