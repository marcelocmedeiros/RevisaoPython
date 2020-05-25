# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 19 Variáveis Composta Dicionários---> GUSTAVO GUANABARA

'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) 
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
print('='*30)
print('{:*^30}'.format(' APOSENTADORIA '))
print('='*30)
print()


# datetime para gerar a data do ano atual
from datetime import datetime
# diconário c\ nome,nascimento, idade e ctps
dados = dict()
dados['Nome'] = str(input('NOME: '))
# vai ser lido mas não cadastrado
nasc = int(input('ANO DE NASCIMENTO: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('N° CTPS (0 se não tem): '))
# vai verificar se ctps tem ou não contratação
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano da contratação: '))
    dados['Salário'] = float(input('SALÁRIO: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('-=' * 20)
# for para imprimir iterado os dados das keys e valures
for k, v in dados.items():
    print(f'   ->   {k} tem o valor {v}')
