# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 12 CONDIÇÕES ANINHADAS ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o ano de nascimento de um atleta e mostre sua categoria 
e acordo com a idade:
    
    até 9 anos: mirim
    até 14 anos: infantil
    até 19 anos: junior
    até 25 anos: sênior
    acima 25: master
'''
print('='*30)
print('{:+^30}'.format(' Categoria Esportiva '))
print('='*30)
print()

from datetime import date

ano = int(input('Informe o ano de nascimento: '))

idade = date.today().year - ano

if idade <= 9:
    print('Sua categoria é Mirin')
elif 9 < idade <= 14:
    print('Sua categoria é Infantil')
elif 14 < idade <= 19:
    print('Sua categoria é Junior')
elif 19 < idade <= 25:
    print('Sua categoria é Sênior')
else:
    print('Sua categoria é Master')
print()
