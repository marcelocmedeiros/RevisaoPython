# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 12 CONDIÇÕES ANINHADAS ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o comprimento de três seguimentos e diga ao usuáro se 
elas podem ou não formar um triângulo.

Acrecentando o recurso de mostrar que tipo de triângulo será formado:
    
    Equilátero: todos os lados iguais
    Isósceles: dos lados iguais
    Escaleno: todos os lados diferentes
'''
print('='*30)
print('{:+^30}'.format(' Categoria de um Triângulo  '))
print('='*30)
print()

linha1 = float(input('Informe o 1° segmento: '))
linha2 = float(input('Informe o 2° segmento: '))
linha3 = float(input('Informe o 3° segmento: '))
print()

# condição para forma triângulo "a < b+c; b < a+c; c < b+a"
if linha1 < linha2 + linha3 and linha2 < linha1 + linha3 and linha3 < linha2 + linha1:
    print(f'Os segmentos {linha1:.0f}, {linha2:.0f} e {linha3:.0f}\n'
          f'Formam um triângulo.')
    #condição para tipo de triângulo
    if linha1 == linha2 == linha3:
        print('Este triângulo é do tipo Equilátero')
    elif linha1 != linha2 != linha3:
        print('Este triângulo é do tipo Escaleno')
    else:
        print('Este triângulo é do tipo Isósceles')
else:
    print(f'Os segmentos {linha1:.0f}, {linha2:.0f} e {linha3:.0f}\n'
          f'Não formam um triângulo.')
print()
