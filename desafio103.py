# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 21 Funções (Def) 2° parte---> GUSTAVO GUANABARA

'''
Faça um Programa que tenha uma função chamada ficha() que receba dois parâmetros
opcionais: o primeiro que indique o nome do jogador e o outro chamado gols que
informe quantos gols ele fez. O programa deverá ser capaz de mostrar a ficha do
jogador mesmo que algum dado não tenha fido informado corretemente.
'''

print('='*30)
print('{:*^30}'.format(' Def ficha()  '))
print('='*30)
print()

# função fatorial, show
def ficha(jog = '<desconhecido>', gol = 0):
    '''
    -> ficha do jogador
    :param nome: nome do atleta
    :param gols: números de gols
    :return: não tem
    '''
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')
    #calculo dao fatorial

# Programa principal
# parâmetro/ argumentos nome e gols
nome = str(input('Digite o nome do jogador: '))
# no lugar de int coloco str para ler números como strings
gols = str(input('Quantos gols o jogador fez: '))
# criando uma condição para converter str em numerico
# se gols for número converte str em int
if gols.isnumeric():
    gols = int(gols)
# se não gols = 0
else:
    gols = 0
# se nome estiver vazio ficha(gol = gols)
if nome.strip() == '':
    ficha(gol = gols)
# se não ficha(nome, gols)
else:
    ficha(nome, gols)


