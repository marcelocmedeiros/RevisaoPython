# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o ano de nascimento de sete pessoas.No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
print('='*30)
print('{:*^30}'.format('  Maioridade  '))
print('='*30)
print()

from datetime import date

cont = 0
soma = 0
for c in range(1, 8):
    ano = (int(input(f'Em que ano {c}° pessoa nasceu: ')))
    idade = date.today().year - ano
    if idade >= 18:
        cont += 1
    else:
        soma += 1
print()
print(f'Ainda não atingiram maior idade: {soma} pessoa(s)\nJá são maiores: {cont} pessoa(s)')
print()
