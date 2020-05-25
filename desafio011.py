# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 07 GUSTAVO GUANABARA

'''
Faça um programa que leia a largura e a altura de uma parede em metros calcule a sua área
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma
área de 2m².
'''
print('='*30)
print('{:$^30}'.format('  LOJA DE TINTA  '))
print('='*30)

largura = float(input('Informe a largura da parade:'))
altura = float(input('Informe a altura da parade:'))
tinta = 2

area = largura * altura
quantid = area / tinta
print()
print('Você informou que a parede tem:\n\n---> A largura de {}m\n---> A altura de {}m\n---> Assim sua área é de {}m²'.format(largura, altura, area))
print('---> A quantidade de tintas a ser usda será de {}l\n'.format(quantid))
