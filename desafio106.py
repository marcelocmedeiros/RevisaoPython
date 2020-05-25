# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 21 Funções (Def) 2° parte---> GUSTAVO GUANABARA

'''
Faça um mini-sistema que utilize o Interactive Help do Python.O usuário vai digitar 
o comando e o manual vai aparecer.Quando o usuário digitar a palavra Fim o programa 
se encerrará.
'''

print('='*40)
print('{:*^30}'.format(' Mini-sistema Interactive Help do Python'))
print('='*40)
print()

# importando sleep de forma global
from time import sleep


# função ajuda que chama comando help
def ajuda(com):
    titulo = (f'Acessando o manual do comando {com}')
    help(com)
    sleep(0.5)
def titulo(msg):
    tam = len(msg)
    print(f'{msg}')
    sleep(1)


#programa principal
comando = ''
while True:
    titulo('Sitema de ajuda Pyhelp')
    comando = str(input('Função ou Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!')
