# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 18 Variáveis Composta Listas 2° parte---> GUSTAVO GUANABARA

'''
Faça um programa que o usuário possa digitar sete valores númericos e cadastre-os em uma lista única 
que matenha separados os valores pares e ímpares.
No final moste os valores pares e ímpares em ordem crescente.
'''
print('='*30)
print('{:*^30}'.format('Pares e Ímpares ordem crescente'))
print('='*30)
print()


# criei uma lista e dentro dela duas lista assim: [[0], [1]]
lista = [[], []]
# variável temporária antes de colocar na lista principal
num = 0
# criando um laço for para fazer uma lista de 7 elementos
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    # condição de par ou ímpar
    if num % 2 == 0:
        # informando em [0] ou [1] que parte da lista quero add o num
        lista[0].append(num)
    else:
        lista[1].append(num)
# colocando a lista em ordem crescente
lista[0].sort()
lista[1].sort()

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')

