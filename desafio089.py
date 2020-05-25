# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 18 Variáveis Composta Listas 2° parte---> GUSTAVO GUANABARA

'''
Faça um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
'''
print('='*30)
print('{:*^30}'.format(' Boletim Completo '))
print('='*30)
print()

ficha = list()
# loop infinito para colocar qualquer quantidade de alunos
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2)/2
    # Lista composta com o append já coloco dentro de uma lista. Dentro outra lista das notas.
    ficha.append([nome, [nota1, nota2], media])
    # caso queria parar Nn
    resp =str(input('Quer continuar[S/N]? '))
    if resp in 'Nn':
        break
# a estrutura do boletim
print('-=' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 30)
# for para cada índice da lista i, aluno
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# loop infinito para mostrar notas do aluno
while True:
    print('-=' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    # a opção tem que ser menor que len(ficha) -1 pq primeiro aluno é 0(índice)
    if opc <= len(ficha) - 1:
        # lembrando que ficha[opc][0] = Nome do aluno e [opc][1] = são as notas
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

