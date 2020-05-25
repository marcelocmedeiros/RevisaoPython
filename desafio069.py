# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 15 LAÇO DE REPETIÇÃO WHILE 2ª parte ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia a idade e o sexo de várias pessoas cadastradas. O programa deverá 
perguntar se o usuário quer ou não continuar. No final mostre:

    a- Quantas pessoas tem mais de 18 anos.
    b- Quantos homens foram cadastrados.
    c- Quantas mulheres tem menos de 20 anos.
    '''
print('='*30)
print('{:*^30}'.format('CADASTRO DE PESSOAS WHILE/BREAK'))
print('='*30)
print()

# contadores 
maior18 = homem = menos20 =0

#loop infnito da idade
while True:
    idade = int(input('Qual sua idade: '))
    #loop infinito só aceita "M ou F"
    sexo = ' '
    while sexo not in 'MF':

        sexo = str(input('Qual o sexo [M]- masculino [F]- feminino: ')).upper().strip()[0]
    # total de maior de 18    
    if idade >= 18:
        maior18 += 1
    # total de homens
    if sexo == 'M':
        homem += 1
    # total de mulheres menores de 20 anos
    if sexo == 'F':
        if idade < 20:
            menos20 += 1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S]- sim e [N]- não:')).strip().upper()[0]
    if resp == 'N':
        break
print('*' * 40)    
print(f'São {maior18} pessoas maiores de 18 anos\n'
f'O total de Homens cadastrado é {homem}\n'
f'Tem {menos20} mulheres menores de 20 anos')
print('*' * 40)





