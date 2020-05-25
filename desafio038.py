# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 12 CONDIÇÕES ANINHADAS ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia dois números e compare-os mostrando na tela uma menssagem:
    
    O primeiro valor é maior
    O segundo valor é maior
    Não existe valor maior ambos são iguais.
'''
print('='*30)
print('{:+^30}'.format(' Comparando Dois Números '))
print('='*30)
print()

num1 = int(input('Informe o 1° número: '))
num2 = int(input('Informe o 2° número: '))
print()

if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior ambos são iguais')
print()
