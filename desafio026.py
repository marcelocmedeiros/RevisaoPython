# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 09 GUSTAVO GUANABARA

'''
Faça um programa leia uma frase e mostre:
1- Quantas vezes aparece a letra "A"
2- Em que posição ela a letra "A" aparece pela primeira vez
3- Em que posição ela a letra "A" aparece pela última vez
'''
print('='*30)
print('{:*^30}'.format('  FRASE '))
print('='*30)
print()

frase = str(input('Escreva uma frase qualquer: ')).strip().lower()

print()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('a')))
print('A letra "A" aparece a primeira vezes na posição {}°'.format(frase.find('a')+1))
print('A letra "A" aparece pela última vezes na posição {}°'.format(frase.rfind('a')+1))
print()
