# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 15 LAÇO DE REPETIÇÃO WHILE 2ª parte ---> GUSTAVO GUANABARA

'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as 
de 1, 5, 10, 50 e 100 reais.

O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais,
        o programa fornece duas notas de 100,
         uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais,
        o programa fornece três notas de 100,
        uma nota de 50, quatro notas de 10,
        uma nota de 5 e quatro notas de 1.
'''
print('='*30)
print('{:*^30}'.format(' Caixa Eletrônico '))
print('='*30)
print()

valor = int(input('Quanto você quer sacar? R$ '))
# variável total é o valor do saque
total = valor
# variável cedula é maior cedula que existe ou pede
cedula = 100
# será o total de cada cedula individualmente
totced = 0
# um loop c infinito que para(breaK) quando total == 0
while True:
    # condiçãos para contar as cedulas
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        # uma condição para escreve só se o total de cedulas for maior que zero
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}')
        if cedula == 100:
            # quando a total for menor que cedula, ela recebe a cedula de menor valor depois dela
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        # para total de cedulas voltar a 0 quando mudar de notas
        totced = 0
        if total == 0:
            break
print('*' * 30)
print('Volte sempre ao Banco!')
print('*' * 30)
