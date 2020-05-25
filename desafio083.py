# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 17 Variáveis Composta Listas ---> GUSTAVO GUANABARA

'''
Faço um programa onde usuário digite uma expressão qualquer que use parênteses. Seu
aplicativo deverá analisar se a expressão passada está com os parentes abertos e fechados na ordem correta
'''
print('='*30)
print('{:*^30}'.format(' Parentes ( e () na Ordem Correta '))
print('='*30)
print()

expr = str(input('Digite sua expressão: '))
# vou criar a lista para condição ver se os parenteses estão corretos ou não
lista = []
# criando um laço for para capiturar cada um simbolo da expressão
for simbolo in expr:
    # se o simbolo for "(" vou add a lista
    if simbolo == '(':
        lista.append('(')
    # se o simbolo for ")" vou verificar se ele fecha "()" ou se está solto ")"
    elif simbolo == ')':
        # len(lista) vai dizer se existe "(" aberto quando len > 0
        if len(lista) > 0:
            # lista.pop vai retirar o último elemento para fechar os parenteses
            lista.pop()
        # se não coloco um ")" que mostra q teve mais ")" do que abrindo
        else:
            lista.append(')')
            break
# se no final len(lista) for igual 0 mostra que não existe parenteses abertos
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está invalida!')
