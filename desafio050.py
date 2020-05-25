# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o.
'''
print('='*30)
print('{:*^30}'.format(' SOMA DOS NÚMEROS PARES '))
print('='*30)
print()

#o acumulador vai informar a soma dos pares
soma = 0
#contador vai informar quantos número pares foram digitados
cont = 0
#for antes da entrada para evitar repetições
for c in range(1, 7):
    num = int(input(f'Informe o {c}° número: '))

    #condição de ser par
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print()        
print(f'Você informou {cont} números pares.\n'
      f'E a soma dos números pares é {soma}.')
print()
