# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 16 Variáveis Composta Tuplas ---> GUSTAVO GUANABARA

'''
Faça uma tupla preenchida com os 20 primeiros colocadosda tabela do
Brasileirão 2019 na ordem de colocação. Depois mostre:
    1- Os cinco primeiros.
    2- Os últimos 4 colocados.
    3- Times em ordem alfabética
    4- Em que posição está o time do Corinthians.
'''
print('='*30)
print('{:*^30}'.format(' Brasileirão 2019 '))
print('='*30)
print()

times = ('Flamengo', 'Santos','Palmeiras', 'Grêmio', 'Athletico-PR',
             'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
         'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'Os cinco primeiros são {times[0:5]}')
print(f'Os últimos 4 colocados são {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'Em que posição está o time do Corinthians: {times.index("Corinthians")+1}° colocado.')