# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que calcule a soma entre todos os números impares que 
são multiplos de três e que se encontrem no intervalo 1 até 500.
'''
print('='*30)
print('{:*^30}'.format(' SOMA DOS IMPARES '))
print('='*30)
print()

#acumulador soma q vai somar todos os impares mult de 3
soma = 0
# contador para informar quantos num existem entre 1 - 500
cont = 0
# dentro do for usei o artificil de começa por um impar e pular de 2 em 2 para continuar nos números impares
for c in range(1, 500, 2):
    # condição de ser multiplo de 3
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print(f'A soma de todos os números impares e multiplos de 3 é {cont} e a soma dele é {soma}')
