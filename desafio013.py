# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 07 GUSTAVO GUANABARA

'''
Faça um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumneto.
'''
print('='*30)
print('{:$^30}'.format('  REAJUSTE 15%  '))
print('='*30)
print()

salario = float(input('Qual o valor do seu salário:R$ '))

reajuste = salario + (salario*0.15)

print()
print('Seu salário era de R$ {:.2f}\nCom reajuste de 15% agora é R${:.2f}'.format(salario, reajuste))
print()