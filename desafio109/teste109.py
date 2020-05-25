import moeda109

p = float(input('Digite o preço: R$ '))
# quando eu chamar True(3° parametro) estou pedindo para todos os preços virem formatados
print(f'A metade de {moeda109.moeda(p)} é {moeda109.metade(p, True)}')
print(f'A dobro de {moeda109.moeda(p)} é {moeda109.dobro(p, True)}')
# parametros p = preço, taxa = 10 ou qualquer valor e formatado = True p ter preço formatado
print(f'Aumentado 10% de {moeda109.moeda(p)} é {moeda109.aumentar(p, 10, True)}')
print(f'Diminuindo 20% de {moeda109.moeda(p)} é {moeda109.diminuir(p, 20, True)}')