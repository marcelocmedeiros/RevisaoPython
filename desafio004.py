# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 06 GUSTAVO GUANABARA
'''
Faça um prigrama que leia algo pelo teclado e mostre na tela o seu 
tipo primitivo e todas as informações possíveis.
'''
valor = input('Digite Algo:')
# todo input retorna um valor string mesmo que seja número

print('O tipo primitivo é', type(valor))
print('Só tem espaço?', valor.isspace())
print('É numérico?', valor.isnumeric())
print('É Alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
