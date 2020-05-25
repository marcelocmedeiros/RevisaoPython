# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o peso de cinco pessoas. No final mostre qual 
foi maior e o menor peso lidos.
'''
print('='*30)
print('{:§^30}'.format(' PESO '))
print('='*30)
print()

#contadores os dois recebem 0 pq 1° laço ontem o maior == menor
maior = 0
menor = 0

# variáveis peso de cinco pessoas
for p in range(1, 6):
    peso = float(input(f'Qual é o peso da {p}° pessoa: '))
    #condição pq 1° laço p1 vai ter o maior e o menor peso (maior == menor)
    if p == 1:
        maior = peso
        menor = peso
    else:
        # se 2°(...) laço peso > maior então maior = peso
        if peso > maior:
            maior = peso
        # ou se 2°(...) laço peso > menor então menor = peso
        if peso < menor:
            menor = peso
print('='*40)
print(f'O maior peso foi de {maior:.2f}Kg.\n'
      f'O menor peso foi de {menor:.2f}Kg.')