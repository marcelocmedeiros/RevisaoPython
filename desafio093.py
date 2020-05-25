# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 19 Variáveis Composta Dicionários---> GUSTAVO GUANABARA

'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai 
ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols 
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o 
total de gols feitos durante o campeonato.
'''
print('='*30)
print('{:*^30}'.format(' Ficha de jogador de futebol  '))
print('='*30)
print()

# dicionário
jogador = dict()
# lista p partidas
partidas = list()
jogador['nome'] = str(input('NOME: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# for p contador quantos gols jogador fez por partida
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
# vou add gols do jogador no dic = jogador
jogador['gols'] = partidas[:]
# creie a soma dos gols feitos
jogador['total'] = sum(partidas)
print('-=' * 20)
print('jogador')
print('-=' * 20)
# for p exibir de forma iterada os valores da keys e valures do dic
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
# len p n° de partidas
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for p imprimir de forma iterada os valores da keys e valures da lista gols dentro do dic jogador
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i + 1}, fez {v} gols.')
print(f'   => Fez um total de {jogador["total"]} gols.')
