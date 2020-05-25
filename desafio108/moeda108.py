# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 22 Modularização---> GUSTAVO GUANABARA

'''
Adaptar o código do exercício 107, criando uma função adicional chamada moeda() que 
corrija me mostre os valores como um valor monetário formatado. 
'''

print('='*30)
print('{:*^30}'.format('  Módulo Moeda108.py '))
print('='*30)
print()
def aumentar(preço = 0, taxa = 0):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço = 0, taxa = 0):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço = 0):
    res = preço * 2
    return res


def metade(preço = 0):
    res = preço / 2
    return res

def moeda(preço = 0, moeda = 'R$'):
    # retorna uma str e onde tiver "." substitui por "," com função replace formatado :.2f
    return f'{moeda}{preço:.2f}'.replace('.', ',')