# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 12 CONDIÇÕES ANINHADAS ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o peso e a altura de uma pessoa.

Calcule seu IMC e mostre seu status de acordo com a tabela abaixo:

    abaixo de 18.5: Abaixo do peso
    entre 18.5 e 25: peso ideal
    25 até 30: sobrepeso
    30 até 40: obesidade
    acima de 40: Obesidade mórbida
'''
print('='*30)
print('{:+^30}'.format(' Condição Coporal IMC '))
print('='*30)
print()

altura = float(input('Informe a sua altura: '))
peso = float(input('Informe seu peso: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Você está Abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc <  30:
    print('Você está com Sobrepeso')
elif 30 <= imc <  40:
    print('Você está com Obesidade')
else:
    print('Você está com Obesidade Mórbida')
print()
