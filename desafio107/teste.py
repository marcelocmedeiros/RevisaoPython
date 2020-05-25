import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'A dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'Aumentado 10% de R${p:.2f} é R${moeda.aumentar(p, 10):.2f}')
print(f'Diminuindo 20% de R${p:.2f} é R${moeda.diminuir(p, 20):.2f}')