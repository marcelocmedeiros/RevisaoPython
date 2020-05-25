# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 14 LAÇO DE REPETIÇÃO WHILE ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia o sexo de uma pessoas, mas só aceite os valores "M" ou "F".
caso esteja errado peça a digitação novamente até ter um valor correto.
'''
print('='*30)
print('{:*^30}'.format(' CADASTRO SEXO "M" e "F" '))
print('='*30)
print()


#variável str qual sexo "M" ou "F". colocar upper[0] pegar a primeira letra
sexo = str(input('Informe seu sexo escrevendo:\n"M" para masculino ou "F" para feminino.\nQual seu sexo: ')).strip().upper()[0]
# loop infinito até digitar M ou F
while sexo not in 'MF':
    sexo = str(input('\nDados invalidos!\nPor favor, informe corretamente seu sexo.\n\nEscrevendo:\n"M" para masculino ou "F" para feminino.\nQual seu sexo:')).strip().upper()[0]
    print()
print(f'Sexo {sexo} registrado com sucesso.')
