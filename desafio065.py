# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 14 LAÇO DE REPETIÇÃO WHILE ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia vários números inteiros pelo teclado. No final da execução mostre 
a média entre todos os valores e qual foi maior e o menor valores lidos. o programa deve 
perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
print('='*30)
print('{:*^30}'.format(' MÉDIA, MAIOR E MENOR '))
print('='*30)
print()

# contadores n /cont / soma
# forma siplificada 
n = cont = soma = 0
resp = 'S'
# um loop de resp se quer contnuar [S] ou [N] == stop
while resp in 'S':
    n = int(input('Digite uma número inteiro: '))
   
    cont += 1
    soma += n
    media = soma / cont
    # cont == 1 só existe um n° então ele é o maior e o menor
    if cont == 1:
        maior = menor = n
    # conparando os demais n° "n"
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    # depois da operação ele pergunta se quer continuar
    resp = str(input('Quer continuar [S]sim e [N]não: ')).upper().strip()[0]
print()
print(f'Foram digitados {cont}\nE a média entre eles é {media:.0f}.\nO maior é {maior}\nO menor é {menor}')
