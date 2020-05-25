# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 17 Variáveis Composta Listas ---> GUSTAVO GUANABARA

'''
Faça um programa que o usuário possa digitar 5 valores númericos e cadastre-os em uma lista já na posição correta de inserção (sem usar função sorted()). No final mostre a lista ordenada na tela.
'''
print('='*30)
print('{:*^30}'.format(' Lista em Ordem S/ Sorted() '))
print('='*30)
print()


valores = list()

for c in range (0, 5):
    num = (int(input(f'Digite o {c+1}° valor: ')))
    # se for o 1 valor ou se for maior que último[-1] uso .append() para add no final
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Valor adicionado ao final da lista')
    else:
        # fazendo laço while para colocar cada valor na sua posição
        # o contador pos vai indicar qual posição será add num
        pos = 0
        # para verificar se do 0 até a última posição onde será inserido o valor
        while pos <= len(valores):
            # vai verificar se num <= valores usando valores[pos]
            if num <= valores[pos]:
                print(f'Adcionado na posição {pos}')
                # se o valor for menor então uso insert(pos, num) para colocar o valor neste local 
                valores.insert(pos, num)
                # paro o while e vou p próximo valor
                break
            # próximo valor
            pos += 1
print(f'Os valores digitados em ordem foram {valores}.')

