# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que mostre na tela uma contagem regressiva para o 
estouro de fogos de artifícios indo de 10 até 0, com uma pausa de 1 
segundo entre eles.
'''
print('='*30)
print('{:*^30}'.format(' Contagem Regressiva '))
print('='*30)
print()

# importar sleep para dar uma pausa
from time import sleep

for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
print('FIM!')
