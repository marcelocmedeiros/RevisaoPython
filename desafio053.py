# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 13 LAÇO DE REPETIÇÃO FOR ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia uma frase qualquer e diga se ela é um palidromo descosidere espaços.
'''
print('='*30)
print('{:*^30}'.format('  Palidromo  '))
print('='*30)
print()

# variáveis recebe uma frase
frase = str(input('Informe escreva uma frase: ')).strip().upper()

# separei a frase por palavras variável "palavras"
palavras = frase.split()

# juntei todas as palavras com variável "junto"
junto = ''.join(palavras)

# inverso vai esta vazio no inicio variável "inverso"
inverso = ''
# com laço for vou fazer passar por todas as letras. 1- com função "len" informar total de letras, mas como o ínidice começa do zero tenho que subtrair 1 do total para o índice das letras serem iguais a total de letras(len). 2- para incluir a última letra q invertido será o 0 tem que colocar até "-1" para add ela. 3- "-1" para ela vir ordenada de trás para frente.
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Sua frase é um Palitromo!')
else:
     print('Sua frase não é um Palitromo!')

