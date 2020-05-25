# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 21 Funções (Def) 2° parte---> GUSTAVO GUANABARA

'''
Faça um Programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que 
indique o número a calcular e o outro chamado show que será um valor lógico(opcional) indicado 
se será mostrado ou não na tela o processo de cálculo do fatorial
'''

print('='*30)
print('{:*^30}'.format(' Def fatorial() '))
print('='*30)
print()

def fatorial(n, show=False):
    '''
    -> calcule o fatorial de um número.
    :param n: o número a ser calculado
    :param show: (opcional) mostrar ou não na tela a conta
    :return: retorna o valor do fatorial de n
    '''
    #calculo dao fatorial
    f = 1
    # laço for decrescendo
    for c in range(n, 0, -1):
        # if para criar na tela o calculo
        if show:
            print(c, end=' ')
            # se c > 1 mostrar 'x'
            if c > 1:
                print('x', end=' ')
            # se c == 1 mostra '='
            else:
                print('=', end=' ')
        f *= c
    return f


# Programa principal
# parâmetro/ argumentos
n = int(input('Digite um número que deseja ver seu fatorial: '))
print(fatorial(n, show=True))