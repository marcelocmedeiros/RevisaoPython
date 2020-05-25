# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o primeiro termo e a razão de uma PA. No final mostre
os 10 primeiros termos dessa progressão.
'''
print('='*30)
print('{:*^30}'.format(' 10ª Primeiros Termos da PA  '))
print('='*30)
print()

# variáveis termo e razão
print('='*40)
termo_1 = int(input('Informe o 1° termo da "P.A.": '))
razao = int(input('Informe a razão desta "P.A.": '))
print()
# formúla da P.A.
pa_10 = termo_1 + 9 * razao
# laço dos 10° termos da P.A.
for c in range (termo_1, pa_10 + 1, razao):
    #print('{}'.format(c), end='-> ')
    print(f'{c}', end='-> ')
print('FIM!')