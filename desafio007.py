# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 07 GUSTAVO GUANABARA
'''
Faça um programa que leia duas notas de um aluno. Calcule a média 
'''
print('='*30)
print('{:=^30}'.format(" MÉDIA "))
print('='*30)

nota1 = float(input('Informe a 1° nota:'))
nota2 = float(input('Informe a 2° nota:'))

media = (nota1+nota2)/2

print('Sua primeira nota foi {}\nSua segunda nota foi {}\nPortanto sua média é {}'.format(nota1, nota2, media))

#segunda opção 
print('Sua primeira nota foi {}\nSua segunda nota foi {}\nPortanto sua média é {}'.format(nota1, nota2, (nota1+nota2)/2))