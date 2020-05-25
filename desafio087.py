# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 18 Variáveis Composta Listas 2° parte---> GUSTAVO GUANABARA

'''
A primore o desafio 86 e mostre:
    1- Soma de todos os valores pares digitados
    2- Soma de todos os valores terceira coluna
    3- O maior valor da segunda linha
'''
print('='*30)
print('{:*^30}'.format(' Matriz 3x3 2ª parte '))
print('='*30)
print()

# faço a estrutura da matriz pois é uma lista dentro de lista
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# variáveis 
somapar = maior2linha = soma3coluna = 0
# laço for para cadastro dos valores da linha
for l in range(0, 3):
    # outro laço for para cadastro dos valores da coluna
    for c in range(0, 3):
        # matriz [l][c] para ele receber da forma da matriz [{l}, {c}] ex: [0, 0]; [0, 1]
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))
# segue outro for para estrutura da matriz
for l in range(0, 3):
    for c in range(0, 3):
        # :^5 centralizado em 5 espaços/ end='' ficar um do lado do outro
        print(f'[{matriz[l][c]:^5}]', end='')
    # verificação dos números pares da matriz e sua soma
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    # esse print para toda vez que quebrar a coluna ele ir para outra linha
    print()
print('-=' * 30)
print(f'A soma dos valores da pares é {somapar}')
for l in range(0, 3):
    #soma dos valores da 3 coluna lembrando sempre que coluna fixa [2] q muda linha
    soma3coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma3coluna}')
for c in range(0, 3):
    # veficando qual mairo número da 2 linha lembrando sempre que linha fixa [1] q muda coluna
    if c == 0:
        maior2linha = matriz[1][c]
    elif matriz[1][c] > maior2linha:
        maior2linha = matriz[1][c]
print(f'O maior valor da segunda linha é {maior2linha}.')
