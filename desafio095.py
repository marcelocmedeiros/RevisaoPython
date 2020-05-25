# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 19 Variáveis Composta Dicionários---> GUSTAVO GUANABARA

'''
Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
print('='*30)
print('{:*^30}'.format(' Ficha de vários jogadores  '))
print('='*30)
print()


time = list ()
# dic para armazenas as cada jogador com suas partidas e gols
jogador = dict()
partidas = list()
# loop p cadastrar quantos jogadores quiser
while True:
    # limpar o nome anterior e receber o novo nome e não acumular
    jogador.clear()
    jogador['nome'] = str(input('NOME: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    # limpar partidas anterior e receber novas partidas do novo jogador e não acumular
    partidas.clear()
    # laço para ver em quais partidas foram feitos os gols
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    # totaliza os gols
    jogador['total'] = sum(partidas)
    #cria um copia do dic jogador para lista time
    time.append(jogador.copy())
    # laço se quer ou não continuar ...
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in'SN':
            break
        print('ERRO! RESPONDA APENAS S OU N.')
    if resp == 'N':
        break
print('-=' * 20)
# começa aqui a visualização do sitema detalhado
print('cod ', end='')
# for mostrar de forma iterada visualização do sitema detalhado
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 20)
# for mostrar de forma iterada as keys e valures
for k, v in enumerate(time):
    print(f' {k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 20)
# laço para informar detalhe do jogador '999 break'
while True:
    busca = int(input('Mostra dados de qual jogador (999 para parar)? '))
    if busca == 999:
        break
    # condição p não buscar valor maior que o da lista time
    if busca >= len(time):
        print(f'ERRO! NÃO EXISTE JOGADOR {busca}!')
    else:
        print(f'  --LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        # for q vai mostrar a fixa do jogar escolhido
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i + 1} fez {g} gols.')
    print('-=' * 30)
print('<<< VOLTE SEMPRE >>>')
