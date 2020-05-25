# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 07 GUSTAVO GUANABARA
'''
Faça um programa que leia um número inteiro e mostre seu dobro, triplo e sua raiz quadrada.
'''
print('='*30)
print('DOBRO, TRIPLO E RAIZ QUADRADA')
print('='*30)

num = int(input('Informe um número:'))

dobro = num*2
triplo = num*3
raiz = num**(1/2)

print('Você digitou {}\nO dobro é {}\nO triplo é {}\nSua raiz quadrada é {}'.format(num, dobro, triplo, raiz))

# outra forma 

#print('Você digitou {}\nO dobro é {}\nO triplo é {}\nSua raiz quadrada é {}'.format(num, num*2, num*3, num**(1/2)))