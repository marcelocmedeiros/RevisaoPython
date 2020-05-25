# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 22 Modularização---> GUSTAVO GUANABARA

'''
Crie um módulo chamado moeda .py que tenha as funções incorporadas aumentar() diminuir(), dobro() 
e metade(). Faça também um programa que importe esses módulos e use algumas dessas funções.
'''

print('='*30)
print('{:*^30}'.format('  Módulo Moeda.py '))
print('='*30)
print()

def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço,taxa):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res