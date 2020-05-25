# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 10 CONDIÇÕES GUSTAVO GUANABARA

'''
Faça um Programa que leia a velocidade de um carro.Se ele ultrapassar 80Km/h 
mostre uma menssagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite.
'''
print('='*30)
print('{:*^30}'.format(' MULTA POR ULTRAPASSAR 80km/h '))
print('='*30)
print()

carro = float(input('A velocidade de seu carro: '))
print()

# bloco de condições caso ultrapasse o limete de 80km/h
if carro > 80:
    multa = (carro - 80) * 7
    print('Você ultrapassou o limete de 80km/h.\nSeu carro estava há {:.0f}km/h.\nSua multa é no valor de R$ {:.2f}.'.format(carro, multa))
else:
    print('Parabéns continue dirigindo assim...\nSua velocidade %dkm/h'%carro)
print()
