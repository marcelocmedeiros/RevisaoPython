# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 15 LAÇO DE REPETIÇÃO WHILE 2ª parte ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia vários números inteiros pelo teclado. O programa só vai parar quando 
o usuário digitar o valor 999 que é a condição de parada. No final mostre quantos números
foram digitados e qual foi a soma entre eles.(desconsiderando o flag)
'''
print('='*30)
print('{:*^30}'.format(' SOMA & PARA COM BREAK '))
print('='*30)
print()

#forma simplificada 
cont = soma = 0
#loop infinito com True
while True:
    n = int(input('Digite uma número inteiro [para parar 999]:'))
    # condição de parar com break
    if n == 999:
        break
    soma += n
    cont += 1

print()
print(f'Foram digitados {cont} e a soma entre eles é {soma}')


