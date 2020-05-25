# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 10 CONDIÇÕES GUSTAVO GUANABARA

'''
Faça um Programa que pergunte o salário do funcionário e calcule o valor do seu aumento.
    * Para salários superiores a R$ 1.250.00, Calcule um aumento de 10%.
    * Para os inferiores ou iguais o aumento é de 15%.
'''
print('='*30)
print('{:$^30}'.format(' AUMENTO DE SALÁRIO '))
print('='*30)
print()

salario = float(input('Qual valor do seu salário: '))
print()

if salario <= 1250:
    reajuste = salario + (salario * 0.15)
    print('Você tinha um salário de R$ %.2f.\nCom reajuste de seu novo salário é R$ %.2f'%(salario, reajuste))

else:
    reajuste = salario + (salario * 0.10)
    print('Você tinha um salário de R$ %.2f.\nCom reajuste de seu novo salário é R$ %.2f.'%(salario, reajuste))
print()
