# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 07 GUSTAVO GUANABARA

'''
Faça um programa que leia uma temperatura em Celsius °C e converta para Fahrenheit °F.
'''
print('='*30)
print('{:#^30}'.format('  TEMPERATURA  '))
print('='*30)
print()

temp = float(input('Informe a temperatuara °C:'))

saida = 1.8*temp + 32

print()
print('A temperatura informada foi de {:.1f}°C\nNa estacala Fahrenheit é {:.1f}°F'.format(temp, saida))
print()
