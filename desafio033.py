# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 10 CONDIÇÕES GUSTAVO GUANABARA

'''
Faça um Programa que leia três números e mostre qual é o maior e qual é o menor.
'''
print('='*30)
print('{:#^30}'.format(' O Maior qual o Menor '))
print('='*30)
print()

num1 = int(input('Informe um 1° número: '))
num2 = int(input('Informe um 2° número: '))
num3 = int(input('Informe um 3° número: '))
print()

'''if num1 > num2 and num1 > num3:
    maior =  num1
    if num2 > num3:
        menor = num3
    else:
        menor = num2
if num2 > num1 and num2 > num3:
    maior =  num2
    if num1 > num3:
        menor = num3
    else:
        menor = num1
else:
    maior = num3
    if num1 > num2:
        menor = num2
    else:
        menor = num1
print('O maior número é %d'%maior)
print('O menor número é %d'%menor)
print()'''

# outra forma 
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O menor número foi {}'.format(menor))
print('O maior número foi {}'.format(maior))