# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 21 Funções (Def) 2° parte---> GUSTAVO GUANABARA

'''
Faça um Programa que tenha uma função chamada notas() que pode eceber várias notas
de alunos e vai retorna um dicionário com as seguites informações:
    - Quantidade de notas
    - Maior nota
    - Menor nota
    - Média da Turma
    - Situação(opcional) adicione também as dostrings
'''

print('='*30)
print('{:*^30}'.format(' Def notas() '))
print('='*30)
print()


# função *n (varias notas) sit =  False por padrão para começar avaliação
def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (*n = aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicioário com varias informações sobre a situação da turma.
    '''
    # criamos um dicionário com informações pedidas
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    # caso requeira a sit o programa informa conforme abaixo
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#programa principal
resp = notas(10, 6, 6, sit=True)
print(resp)
#help(notas)