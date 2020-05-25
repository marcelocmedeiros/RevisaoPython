# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 19 Variáveis Composta Dicionários---> GUSTAVO GUANABARA

'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
 Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
 sabendo que o vencedor tirou o maior número no dado.
'''
print('='*30)
print('{:*^30}'.format(' Jogodo de Dados '))
print('='*30)
print()


# importando funç. randint p gerar resultados aleatórios
from random import randint
# funç.sleep p criar um espaço de tempo
from    time import sleep
# funç. itemgetter para ordenar por item
from operator import itemgetter
# criar o dicionário com 4 jogadores
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
# criei um dicionário ranking p armazenar a ordem
ranking = list()
print('Valores Sorteados:')
# um for para mostrar cada keys e seu valures em iterado
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
# sorted para colocar em ordem decrescente (reverse=True)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('   == RANKING DOS JOGADORES ==   ')
# for para imprimir iterado conforme valores
# lembrando q usei enumerate pq peguei os valores de ranking = list()
for i, v in enumerate(ranking):
    print(f'  {i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
