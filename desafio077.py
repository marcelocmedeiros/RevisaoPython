# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 16 Variáveis Composta Tuplas ---> GUSTAVO GUANABARA

'''
Faça um programa que tenha uma tupla com várias palavras(não usar acentos).
Depois disso, você deve mostrar para cada palavra quais são as suas vogais.
'''
print('='*30)
print('{:*^30}'.format(' Mostra as Vogais '))
print('='*30)
print()

palv = ('arara', 'sapo', 'pipa','mae', 'uva', 'ovo')

for p in palv:
    print(f'\nNa palavras {p.upper()} temos ', end='') #\n quebra a linha
    # for passa letra por letra 
    for letra in p:
        # se for vo
        if letra.lower() in 'aeiou':
            print(letra, end='')
print()
print()