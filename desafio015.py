# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 07 GUSTAVO GUANABARA

'''
Faça um programa que pergunte a quantidade de kilometros percorridos por um carro alugado 
e a quantidade de dias pelo quais ele permaneceu alugado. Calcule o preço a pagar, sabendo 
que o carro custa R$ 60.00 por dia e 0.15 por kilometros rodados. 
'''
print('='*30)
print('{:$^30}'.format('  LOCADORA DE VEÍCULO  '))
print('='*30)
print()

km = float(input('Qual a quantidade de Kilometros percorridos:'))
dias = int(input('Quantos dias você permaneceu com o carro:'))

valor = (km * 0.15) + (dias * 60)

print()
print('Você permaneceu com o carro por {} dias\nO carro percurreu {:.2f}km\nO valor da locação é R$ {:.2f}'.format(dias, km, valor))
print()
