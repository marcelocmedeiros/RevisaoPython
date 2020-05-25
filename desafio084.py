# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 18 Variáveis Composta Listas 2° parte---> GUSTAVO GUANABARA

'''
Faça um programa que leia nome e peso de várias pessoas. Guardando tudo em uma lista.
No final mostre:
 1- Quantas .
 2- Uma listagem com as pessoas mais pesadas.
 3- Uma listagem comas pessoas mais leves.
'''
print('='*30)
print('{:*^30}'.format('  LISTAGEM DE PESSOA E PESO '))
print('='*30)
print()

#criei um lista temporaria para ela ser incliuida na lista pricipal
temporaria = list()
principal = list()
maior = menor = 0
# laço inifinito para cadastrar quantas pessoas quiser
while True:
    temporaria.append((str(input('Nome: '))))
    temporaria.append((float(input('Peso: '))))
    # compração dos pesos maior e menor
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    # fiz uma copia da lista temporaria dentro da principal
    principal.append(temporaria[:])
    # limpei a lista temporaria para não duplicar os valores
    temporaria.clear()
    # quando o quiser mais cadastrar Nn para o programa
    resp = str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
# len(principal) para contar quantos ítens existe na lista
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
# criando as lsita de maior e menor peso (p[0] = nome e p[1] = peso)
print(f'O maior peso foi de {maior:.0f}Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor:.0f}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()


