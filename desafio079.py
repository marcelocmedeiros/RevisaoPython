# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 17 Variáveis Composta Listas ---> GUSTAVO GUANABARA

'''
Faça um programa que o usuário possa digitar varios valores númericos e cadastre-os em uma lista. Caso o número já exista na lista ele não será adicionado.
No final serão exibidos todos os valores únicos em ordem crescente.
'''
print('='*30)
print('{:*^30}'.format(' CADASTRODE VALORES EM LISTA '))
print('='*30)
print()

# variável valores recebe lista
valores = list()
# função sort coloca os valor em ordem crescente
valores.sort()
# while True para laço infinito pedindo valores
while True:
    num = int(input('Digite um valor: '))
    # condição para os valores serem add na lista
    if num not in valores:
        valores.append(num)
        print('Valor add com Sucesso!')
    else:
        print('Valor já foi adcionado digite outro valor!')
    # para o prog. parar deve escolher Não
    resp = str(input('Quer continar [S]IM e [N]ÃO: ')).strip().upper()
    if resp in 'N':
        break

print(f'\nVocê digitou os valores {valores}\n')

