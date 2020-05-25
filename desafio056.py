# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o nome, idade e sexo de 4 pessoas.

No final do programa mostre:
    a média de idade do grupo
    qual é nome do homem mais velho
    quantas mulheres têm menos de 20 anos.
'''
print('='*30)
print('{:*^30}'.format(' CADASTRO DE PESSOAS '))
print('='*30)
print()

#contadores soma da idade - média da idade - maior idade de homem
# nome velho - total mulheres 20
soma_idade = 0
media_idade = 0
maior_idade_h = 0
nome_velho = ' '
total_mul_20 = 0

# variáveis nome, idade e sexo de 4 pessoas
print('='*40)
for p in range(1, 5):
    print(f'--------{p}ª PESSOA--------')
    nome = str(input('NOME: ')).strip().upper()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    # soma das idades
    media_idade = soma_idade / 4
    #condição quando p == 1 do sexo M o mais velho é ele
    if p == 1 and sexo in 'M':
        maior_idade_h = idade
        nome_velho = nome
    # comparando pessoas do sexo M se idade > se sim maior = idade e nome_velho = nome
    if sexo in 'M' and idade > maior_idade_h:
        maior_idade_h = idade
        nome_velho = nome
    # condição p for sexo F e idade < 20 soma contadora + 1 para mostrar no final o total de F < 20
    if sexo in 'F' and idade < 20:
        total_mul_20 += 1
# média das idades
media_idade = soma_idade / 4
print()
print(f'A média de idade do grupo é {media_idade:.2f}.\n'
      f'O nome do homem mais velho é {nome_velho}.\n'
      f'O número de mulheres têm menos de 20 anos é {total_mul_20}')
print()