# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 10 CONDIÇÕES GUSTAVO GUANABARA

'''
Faça um Programa que pegunte a distância de uma viagem em Km.
Calcule o peço da passagem cobrando R$ 0.50 por Km para viagens
até 200Km e R$ 0.45 para viagens mais longas.
'''
print('='*30)
print('{:$^30}'.format(' Peço da Passagem '))
print('='*30)
print()

distancia = float(input('QUal a distância de uma viagem? '))
print()

#condição do preço da passagem até 200km 0.50 por km maior 0.45 por km
if distancia <= 200:
    valor = distancia * 0.50
    print('A sua passagem custou R${:.2f}'.format(valor))
else:
    valor =  distancia * 0.45
    print('A sua passagem custou R$%.2f'%valor)