# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 16 Variáveis Composta Tuplas ---> GUSTAVO GUANABARA

'''
Faça um programa que tenha uma tupla única com nome de produtos e seus respectivos preços na sequência. 
No final mostre uma listagem de preços orgnizados os dados em forma tabuladar
'''
lista = ('Lapis', 1.75,
         'Borracha', 2,
         'caderno', 18.5,
         'compasso', 10,
         'canetas', 22.7)

print('-' * 40)
print(f' {"LISTAGEM DE PREÇO":^40}')
print('-' * 40)

for pos in range(0, len(lista)):
    # caso posição seja par vou alinhar a esquerda .<30
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    # impar alinho a direita e formatado com R$ ".2f"
    else:
        print(f'R${lista[pos]:>7.2f}')

print('-' * 40)
