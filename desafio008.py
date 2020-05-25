# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 07 GUSTAVO GUANABARA
'''
Faça um programa que leia uma valor em metros e exiba convertendo em centimetros e milímetros. 
'''
print('='*30)
print('{:=^30}'.format('CONVERSO DE MEDIDAS m, cm, mm '))
print('='*30)

metro = float(input('Informe o valor em metros:'))

cent = metro * 100
mili = metro * 1000

print('Você digitou {:.2f} metros\nConvertido para centímetros é {:.2f}cm\nConvertido para milímetros é {:.2f}mm'.format(metro, cent,mili))

# outra forma 

print('Você digitou {:.2f} metros\nConvertido para centímetros é {:.2f}cm\nConvertido para milímetros é {:.2f}mm'.format(metro, metro*100, metro*1000))