# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 12 CONDIÇÕES ANINHADAS ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o ano de nascimento de um jovem e informe de acordo 
com sua idade se ele ainda vai se alistar ao serviço militar, se é a hora de 
se alistar ou se já paasou do tempo do seu alsitamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
print('='*30)
print('{:+^30}'.format('Alistamento do Serviço Militar'))
print('='*30)
print()

from datetime import date

ano  =  int(input('Em que ano você nasceu: '))

idade = date.today().year - ano

if idade < 18:
    print('Vocâ tem {} anos e só vai se alista em {}'.format(idade, ano + 18))
elif idade > 18:
    print('Vocâ tem {} anos e já passou data do seu alistamento que foi no ano {}'.format(idade, ano + 18))
else:
    print('Você completa 18 anos este ano e deve se alistar no Serviço Militar obrigatório!')
print()
