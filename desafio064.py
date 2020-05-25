# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 14 LAÇO DE REPETIÇÃO WHILE ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia vários números inteiros pelo teclado. O programa só vai parar 
quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos 
números foram digitados e qual foi a soma entre eles (desconsidere o flag)
'''
print('='*30)
print('{:*^30}'.format(' SOMA ATÉ DIGITAR 999 '))
print('='*30)
print()

# contadores n /cont / soma
# forma siplificada n = cont = soma = 0
n = 0
cont = 0
soma = 0 
# um loop de n até digitar 999
while n != 999:
    n = int(input('Digite uma número inteiro [para parar 999]: '))
    if n != 999:
        cont += 1
        soma += n
    
print(f'Foram digitados {cont} e a soma entre eles é {soma}')
