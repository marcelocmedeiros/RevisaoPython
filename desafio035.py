# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 10 CONDIÇÕES GUSTAVO GUANABARA

'''
Faça um Programa que leia o comprimento de três seguimentos 
e diga ao usuáro se elas podem ou não formar um triângulo.
'''
print('='*30)
print('{:+^30}'.format(' Condição para forma Triângulo '))
print('='*30)
print()

linha1 = float(input('Informe o 1° segmento: '))
linha2 = float(input('Informe o 2° segmento: '))
linha3 = float(input('Informe o 3° segmento: '))
print()

# condição para forma triângulo "a < b+c; b < a+c; c < b+a"
if linha1 < linha2 + linha3 and linha2 < linha1 + linha3 and linha3 < linha2 + linha1:
    print('Os seguimentos digitados foram um TRIÂNGULO!')
else:
    print('Os seguimentos digitados NÃO FORMAM UM TRIÂNGULO!')
print()
