# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 17 Variáveis Composta Listas ---> GUSTAVO GUANABARA

'''
Faça um programa que o usuário possa digitar varios valores númericos
e cadastre-os em uma lista. Depois crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados.
Ao final mostre o conteúdo das três listas geradas.
'''
print('='*30)
print('{:*^30}'.format(' Criar uma lista e mostra 3 '))
print('='*30)
print()

valores = list()
par = list()
impar = list()

# while True para laço infinito pedindo valores
while True:
    valores.append(int(input('Digite um valor: ')))
    # para o prog. para deve escolher Não
    resp = str(input('Quer continar [S]IM e [N]ÃO: ')).strip().upper()
    if resp in 'N':
        break
# criei umlaço for para testa valores pares e impares dentro da lista criada
for i, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista dos valores digitados foi {valores}\n'
      f'A lista dos números pares é {par}\n'
      f'A lista do números ímpares é {impar}')
