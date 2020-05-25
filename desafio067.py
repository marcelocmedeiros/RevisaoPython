# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 15 LAÇO DE REPETIÇÃO WHILE 2ª parte ---> GUSTAVO GUANABARA

'''
Faça um Programa que moste a tabuada de vários números um de cada vez para cada valor 
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
print('='*30)
print('{:*^30}'.format(' TABUADA DE VÁRIOS NÚMEROS '))
print('='*30)
print()

while True:
    n = int(input('Informe qualvalor da tabuada: '))
    print()
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:2} = {n * c:2}')
print()   
    