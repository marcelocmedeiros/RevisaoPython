# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 07 GUSTAVO GUANABARA
'''
Faça um prigrama que leia um número inteiro e mostre na tela o seu sucesor e seu antecessor.
'''

num = int(input('Ditite um número:'))

#sucessor = num + 1
#antecessor = num - 1

#print('Você digitou o número {}\nSeu sucessor é {}\nSeu antecesor é {}'.format(num, sucessor, antecessor))

# forma mais simples
print('Analisando o número {}\nSeu sucessor é {}\nSeu antecesor é {}'.format(num, num+1, num-1))