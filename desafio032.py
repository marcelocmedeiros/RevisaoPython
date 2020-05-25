# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 10 CONDIÇÕES GUSTAVO GUANABARA

'''
Faça um Programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
print('='*30)
print('{:#^30}'.format(' ANO BISSEXTO '))
print('='*30)
print()

ano  = int(input('Informe o ano: '))
print()

# condição para ser bissexto ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano %d é BISSEXTO!'%ano)
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))
print()