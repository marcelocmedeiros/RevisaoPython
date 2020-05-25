# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 23 Tratamento de Erros---> GUSTAVO GUANABARA

'''
Escreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da 
digitação de um número de tipo inválido. Aproveitando crie também uma função leiaFloat() 
com a mesma finalidade. 
'''

print('='*40)
print('{:*^30}'.format('  Função leiaInt() e leiaFloat() '))
print('='*40)
print()

# 1° def n° inteiro
def leiaInt(msg):
    # loop infinito p digitar n° correto 
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário prefiriu não digitar nenhum número.\033[m')
            return 0
        else:
            return n

# 2° def n° float
def leiaFloat(msg):
    # loop infinito p digitar n° correto 
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário prefiriu não digitar nenhum número.\033[m')
            return 0
        else:
            return n


#programa principal
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o realfoi {n2}.')
