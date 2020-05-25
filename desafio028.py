# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 10 CONDIÇÕES GUSTAVO GUANABARA

'''
Escreva um Programa que faça o computador pensar em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi número escolhido pelo computador.
O programa deverá escrever na tela se usuário venceu ou perdeu.
'''
print('='*30)
print('{:#^30}'.format('  JODO DA ADVINHAÇÃO '))
print('='*30)
print()

#importando o modulo random 
import random
print('Vou pensar em um número entre 0 e 5...')

pc = random.randint(0, 5)

jogador = int(input('Qual número eu pensei? '))
print()
# bloco de condições True e False
if jogador == pc:
    print('Parabéns você venceu!\nEu tinha pensado no número %d'%pc)
else:
    print('Infelismente você perdeu!\nEu tinha pensado no número %d'%pc)
print()
