# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que mostrando a tabuada de um números que o usuário escolher 
só que agora utilizando um laço for.
'''
print('='*30)
print('{:*^30}'.format(' Tabuada Laço For '))
print('='*30)
print()

num = int(input('Qual valor você quer a tabuada: '))
print()

for c in range (1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
print('Fim!')