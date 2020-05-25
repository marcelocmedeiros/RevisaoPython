# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 14 LAÇO DE REPETIÇÃO WHILE ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia dois valores e mostre um menu como
abaixo:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
Seu programa deverá realizar a operação solicitada em cada caso.
'''
print('='*30)
print('{:*^30}'.format(' CALCULADORA MULTIPLA '))
print('='*30)
print()

# variável num_1 e num_2
num_1 = float(input('Digite o primeiro número: '))
num_2 = float(input('Digite o segundo número: '))

# contador das opções
opcao = 0
#loop infinito até digitar uma das opções do menu
while opcao != 5:
    print('[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] SAIR DO PROGRAMA')
    opcao = int(input('Qual é sua opção: '))
    if opcao == 1:
        soma = num_1 + num_2
        print(f'A soma entre {num_1} + {num_2} é {soma}')
    elif opcao == 2:
        multiplicação = num_1 * num_2
        print(f'A multiplicação entre {num_1} x {num_2} é {multiplicação}')
    elif opcao == 3:
        if num_1 > num_2:
            maior = num_1
            print(f'O {num_1} maior que {num_2}')
        else:
            maior = num_2
            print(f'O {num_2} maior que {num_1}')
    elif opcao == 4:
        print('Informe quais os novos números')
        num_1 = float(input('Digite o 1° número: '))
        num_2 = float(input('Digite o 2° número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida tente novamente!')
    print('='*25)
print('Fim do programa! Volte Sempre!')