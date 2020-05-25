# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 18 Variáveis Composta Listas 2° parte---> GUSTAVO GUANABARA

'''
FFaça um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado. No final mostre a matriz na tela com formatação correta.
'''
print('='*30)
print('{:*^30}'.format('  Matriz 3x3  '))
print('='*30)
print()

# faço a estrutura da matriz pois é uma lista dentro de lista
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
    # esse print para toda vez que quebrar a coluna ele ir para outra linha
    print()