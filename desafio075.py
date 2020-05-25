# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 16 Variáveis Composta Tuplas ---> GUSTAVO GUANABARA

'''
Faça um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final moste:
    1- Quantas vezes apareceu o valor 9
    2- Em que posição foi digitado o 1º valor "3"
    3- Quais foram os números pares
'''
print('='*30)
print('{:*^30}'.format(' 4 valores em uma tupla. '))
print('='*30)
print()

# dentro da variável num vou pedir 4x que digite um número
# , \ para pular uma linha
num = int(input('Digite o 1º número: ')),\
      int(input('Digite o 2º número: ')),\
      int(input('Digite o 3º número: ')),\
      int(input('Digite o 4º número: '))

print(f'Você digitou os números: {num}')
# vou usar count(9) para contar quantas vezes o  nº nove apareceu
print(f'Quantas vezes apareceu o valor 9: {num.count(9)}')
# indentificando se 3 apareceu ou não
if 3 in num:
    print(f'Em que posição foi digitado o 1º valor "3": {num.index(3)+1}° posição')
else:
    print('O "3" não foi  digitado!')
# indentificando se existe número par
print('Os números pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')


