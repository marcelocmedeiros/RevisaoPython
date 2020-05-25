# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 15 LAÇO DE REPETIÇÃO WHILE 2ª parte ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final mostre:

    a- Qual é o total gasto na compra.
    b- Quantos produtos custam mais de R$ 1.000.
    c- Qual é o nome do produto mais barato.
'''
print('='*30)
print('{:*^30}'.format(' TOTAL DAS COMPRAS '))
print('='*30)
print()

# contadores 
totalC = maiorMil =cont =menor = 0
barato = ' '
#loop infinito até resp "N"
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Qual valor: '))
    cont += 1
    totalC += preco
    if preco >= 1000:
        maiorMil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    # break quando resp "N"
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [s]->sim, [N]->não: ')).upper().strip()[0]
    if resp == 'N':
        break
print('*' * 40)
print(f'Total de itens comprados foram {cont}.\n'
f'Total do valor das compras foi R$ {totalC:.2f}.\n'
f'Total de produtos acima de R$ 1.000, é {maiorMil}\n'
f'O produto mais barato foi {barato}')
print('*' * 40)
