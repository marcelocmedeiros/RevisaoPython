# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 12 CONDIÇÕES ANINHADAS ---> GUSTAVO GUANABARA

'''
Faça um Programa que leia duas notas de um aluno e calcule a sua média, 
mostrando uma mensagem no final de acordo com a média atingida:
    
    média abaixo de 5.0: REPROVADO
    média entre 5.0 a 6.9: RECUPERAÇÃO
    média igual ou superior a 7.0: APROVADO
'''
print('='*30)
print('{:+^30}'.format(' Média com Mensagem '))
print('='*30)
print()

nota1 = float(input('Informe sua 1° nota: '))
nota2 = float(input('Informe sua 2° nota: '))
print()

media = (nota1 + nota2)/2

if media < 5:
    print('Sua média foi %.2f e você foi REPROVADO!'%media)
elif media >= 7:
    print('Sua média foi %.2f e você está APROVADO!'%media)
else:
    print('Sua média foi %.2f e você está em RECUPERAÇÃO!'%media)
print()
