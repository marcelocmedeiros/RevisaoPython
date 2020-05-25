# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 14 LAÇO DE REPETIÇÃO WHILE ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia um número qualquer e mostre o seu fatorial.
Ex: 4! = 4x3x2x1= 24
'''
print('='*30)
print('{:*^30}'.format(' FATORIAL COM WHILE '))
print('='*30)
print()

# variável num
num = int(input('Digite o primeiro número: '))

# contador de um fatorial sempre começa com seu número e vai subtraindo -1
c = num
# variável f = 1 pq 1 elemento neutro da multiplicação
f = 1
print(f'O fatorial de {num}! = ', end='')
# o loop vai continuar até c == 1
while c > 0:
    # end=' ' para todos ficarem na mesma linha junte com proximo print
    print(f'{c}',' x ' if c > 1 else ' = ', end=' ')
    f = f * c
    c -= 1
print(f'{f}')
