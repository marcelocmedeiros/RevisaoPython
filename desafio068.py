# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 15 LAÇO DE REPETIÇÃO WHILE 2ª parte ---> GUSTAVO GUANABARA

'''
Faça um Programa que jogue par ou impar com o computador. O jogo só será interropido quando 
o jogador perder. Mostre o total de vitórias que jogador conquistou no final do jogo.
'''
print('='*30)
print('{:*^30}'.format(' JOGO DE PAR OU ÍMPAR '))
print('='*30)
print()

# importa randint
from random import randint

# contador de vitórias
v = 0

# um loop infinto até jogador perder
while True:
    print('*' * 20)
    jogador = int(input('Digite um valor: '))
    print('*' * 20)

    # sortear de 0-10 como valor escolhido do pc
    pc = randint(0,10)
    # contador de total de jogadas
    total = jogador + pc
    # tipo vai receber par ou ímpar
    tipo = ' '

    # um loop informando que enquanto nãofor "P ou I" repete a pergunta 
    while tipo not in 'PI':
        tipo = str(input('[P]- PAR OU [I]- ÍMPARA: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computaador {pc}.\n'
          f'Total deu {total}.', end=' ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')

    # condição p mostrar quem venceu!
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('*'*40)
print(f'GAME OVER! Você venceu {v} vezes.')
print('*'*40)

