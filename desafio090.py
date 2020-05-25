# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 19 Variáveis Composta Dicionários---> GUSTAVO GUANABARA

'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
print('='*30)
print('{:*^30}'.format(' Boletim Completo '))
print('='*30)
print()


aulo = dict()
# variáveis nome e média de um aluno
aulo['nome'] = str(input('Nome: '))
aulo['media'] = float(input(f'A média do {aulo["nome"]} é: '))
# if analisa a situação do aulo
if aulo['media'] >= 7:
    aulo['situacao'] = 'APROVADO!'
elif 5 <= aulo['media'] < 7:
    aulo['situacao'] = 'RECUPERAÇÃO!'
else:
    aulo['situacao'] = 'REPROVADO!'
print('-=' * 20)
# um laço d for para mostrar cada keys e seu valures em iterado
for k, v in aulo.items():
    print(f'-{k} é igual a {v}')
    