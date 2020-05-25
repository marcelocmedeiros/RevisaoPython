# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 19 Variáveis Composta Dicionários---> GUSTAVO GUANABARA

'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
'''
print('='*30)
print('{:*^30}'.format(' Cadastro de Pessoas '))
print('='*30)
print()

# lista para ser usada durante a execução do programa
galera = list()
# dic print final
pess = dict()
soma = média = 0
# while para guarda n° infinito de cadastro pessoa
while True:
    # tem q a pagar a pesso anterior p receber a nova
    pess.clear()
    pess['nome'] = str(input('NOME: '))
    # faz loop pedindo novamente sexo M ou F
    while True:
        # .upper()[0] tudo maiscúlo e só pega 1° letra
        pess['sexo'] = str(input('SEXO: [M/F] ')).upper()[0]
        # validação sexo caso não digite M ou F
        if pess['sexo'] in 'MF':
            break
        print('ERRO! por favor digite apenas M ou F.')
    pess['idade'] = int(input('IDADE: '))
    # soma de de todas as idades
    soma += pess['idade']
    # copia da pessoa ".copy()" pq vai copia dic
    galera.append(pess.copy())
    # faz loop perguntando se quer continuar "se N break"
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        # validação resp caso não digite S ou N
        if resp in 'SN':
            break
        print('ERRO! por favor digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
# len(galera) total pessoas cadastradas
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
# calculo da média das idades
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos')
# lembrando end=' ' para não quebrar a linha juntando com próximo print
print('C) As mulheres cadastradas foram ', end='')
# for para separar pessoas do sexo feminino
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print() # quebra uma linha
print('D) Lista das pessoas que estão acima da média: ')
# for para separa as pessoas acima da média de idade
for p in galera:
    if p['idade'] >= média:
        print('    ', end=' ')
        # for fazer uma listagem das pessoas com os dados do dicionário
        for k, v in p.items():
            print(f'{k} = {v}', end=', ')
        print()
print('<< ENCERRADO >>')
