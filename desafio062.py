# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 14 LAÇO DE REPETIÇÃO WHILE ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o primeiro termo e a razão de uma P.A.
Mostrando os 10 primeiros termos da progressão usando while.
Depois pergunte para o usuário se ele quer o mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
print('='*30)
print('{:*^30}'.format(' P.A. 10 Primeiros Termos '))
print('='*30)
print()

# variáveis 1° termo e razão da P.A.
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da P.A.: '))

# contador
termo = primeiro
cont = 1
total = 0
# lembrando que o programa pede os primeiros 10 termos por isso mais = 10
mais = 10

#loop até digitar 0
while mais != 0:
    total = total + mais
    # loop de 1 até 10
    while cont <= total:
        # lembrando o end= '' serve para juntar os dois prints
        print(f'{termo} ->', end='')
        termo += razão
        cont += 1
    print(' Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')

