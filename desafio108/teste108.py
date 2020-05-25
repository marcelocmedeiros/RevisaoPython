import moeda108

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.metade(p))}')
print(f'A dobro de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.dobro(p))}')
print(f'Aumentado 10% de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.aumentar(p, 10))}')
print(f'Diminuindo 20% de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.diminuir(p, 20))}')
