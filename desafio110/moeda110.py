# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 22 Modularização---> GUSTAVO GUANABARA

'''
Adicione ao módulo moeda.py criado nos desafios anteriores uma função chamada resumo(), 
que mostre na tela algumas informações geradas pelas funções que já temos nos módulos 
criados até aqui. 
'''

print('='*30)
print('{:*^30}'.format('  Módulo Moeda110.py '))
print('='*30)
print()

def aumentar(preço = 0, taxa = 0, formatado = False):
    res = preço + (preço * taxa/100)
    return res if formatado is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formatado = False):
    res = preço - (preço * taxa/100)
    return res if formatado is False else moeda(res)


def dobro(preço = 0, formatado = False):
    res = preço * 2
    return res if not formatado else moeda(res)


def metade(preço = 0, formatado = False):
    res = preço / 2
    return res if not formatado else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço = 0, taxaa = 10, taxar = 5):
   print('=' * 30)
   # .center para centralizar string
   print('RESUMO DO VALOR'.center(30))
   print('=' * 30)
   # \t tab \t\t 2tab
   print(f'Preço analisado: \t{moeda(preço)}')
   print(f'O dobro do preço: \t{dobro(preço, True)}')
   print(f'A metade do preço: \t{metade(preço, True)}')
   print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
   print(f'{taxar}% de redução: \t\t{diminuir(preço, taxar, True)}')
   print('=' * 30)