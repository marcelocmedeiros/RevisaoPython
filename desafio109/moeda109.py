# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 22 Modularização---> GUSTAVO GUANABARA

'''
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvida no desafio 108. 
'''

print('='*30)
print('{:*^30}'.format('  Módulo Moeda109.py '))
print('='*30)
print()

# def passa ter 3 parametros preço taxa e formatado(foramtado=False) p
def aumentar(preço = 0, taxa = 0, formatado = False):
    """ Módulo def de moeda formatado

    Keyword Arguments:
        preço vai receber o valor 
        taxa vai receber a porcentagem
        formatado inicia com {False} sem formatação

    Returns:
        operação --> res if formatado is False else moeda(res)
    """
    res = preço + (preço * taxa/100)
    # retorna res se False/ se não retorne moeda(res)
    return res if formatado is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formatado = False):
    res = preço - (preço * taxa/100)
    return res if formatado is False else moeda(res)


def dobro(preço = 0, formatado = False):
    res = preço * 2
    # if not formatado == if formatado is False
    return res if not formatado else moeda(res)


def metade(preço = 0, formatado = False):
    res = preço / 2
    return res if not formatado else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')