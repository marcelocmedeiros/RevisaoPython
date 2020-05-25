# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 17 Variáveis Composta Listas ---> GUSTAVO GUANABARA

'''
Faça um programa que leia 5 valores númericos e guarde em uma lista.
No final mostre qual foi o maior e o menor valor digitados e as suas respectivas posições na lsita
'''
print('='*30)
print('{:*^30}'.format(' LISTA DE 5 VALORES '))
print('='*30)
print()

# variável valores que vai receber os valores (valores.append)
valores = list()
# maior e menor começão com zero pq inicia o loop e no 1° maior = menor
maior = 0
menor = 0
# o laço for foi usado p add valores a lista valores
for cont in range(0, 5):
    # a funação ".append" serve para acrescentar valores a lista
    valores.append(int(input(f'Digite o {cont + 1}º valor: ')))
    
    # no 1° loop o maior e menor número são iguais 
    if cont == 0:
        maior = menor = valores[cont]
    # no 2° loop o maior e menor são comparados com novo valor(valores.append)
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'\nVocê digitou os valores {valores}')
# este print foi colcalo aqui para evitar repetições na hora da informação mostrada na tela
print(f'O maior valor digitado foi {maior} nas posições', end='')
#  a funação "enumerate" serve para informa qual a opsição dos valores na lista
for i, v in enumerate(valores):
    if  v == maior:
        # este print pode se repetir mais de uma vez pois valores pode ser iguais
        print(f' {i+1}...')
print(f'O menor valor digitado foi {menor} nas posições', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i+1}...\n')

    
        
