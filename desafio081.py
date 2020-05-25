# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 17 Variáveis Composta Listas ---> GUSTAVO GUANABARA

'''
Faça um programa que o usuário possa digitar valorios valores númericos
e cadastre-os em uma lista. No final mostre:
    1- Quantos números foram digitados
    2- A lista de valores ordenada de foram descrecente
    3- Se o valor "5" foi digitado e está ou não na lista.
'''
print('='*30)
print('{:*^30}'.format(' Cadastro de Valores '))
print('='*30)
print()

valores = list()

# while True para laço infinito pedindo valores
while True:
    valores.append(int(input('Digite um valor: ')))
    # para o prog. para deve escolher Não
    resp = str(input('Quer continar [S]IM e [N]ÃO: ')).strip().upper()
    if resp in 'N':
        break
# usei a função len() para contar os valores da lista
print(f'\nVocê digitou os valores {len(valores)}')
# fazer a lista se ordenar por ordem decrecente
valores.sort(reverse=True)
print(f'A lista na ordem descrecente é {valores}')
# verificar se o 5 foi ou nãodigitado
if 5 in valores:
    print('O valor "5" foi digitado e está na lista.')
else:
    print('Valor "5" não foi digitado e não está na lista.\n')
