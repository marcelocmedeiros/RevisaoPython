# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 21 Funções (Def) 2° parte---> GUSTAVO GUANABARA

'''
Faça um Programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de 
nascimento de uma pessoa, retornando um valor literal indicado se uma pessoa tem voto Negado, 
Opicional ou Obrigatório nas eleições.
'''

print('='*30)
print('{:*^30}'.format(' Def voto() '))
print('='*30)
print()

# função voto parâmetro o ano de nascimento
def voto(ano):
    # importando funções datetime para atribuir o ano atual
    # colocando dentro da função para economzar memoria do programa (variável local)
    from datetime import date
    #calculo da idade
    idade = date.today().year - ano
    # condições de obrigatoriedade do vot
    if idade < 16:
        print(f'Com {idade} anos de idade você não direito a voto.')
    elif idade >= 18 and idade < 70:
        print(f'Com {idade} anos de idade o é voto obrigatório.')
    else:
        print(f'Com {idade} anos de idade o voto é opcional.')


# Programa principal
#variável ano
ano = int(input('Em que ano você nasceu: '))
# imprima função voto
print(voto(ano))


