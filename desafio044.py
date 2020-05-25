# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 12 CONDIÇÕES ANINHADAS ---> GUSTAVO GUANABARA

'''
Faça um Programa que calcule o valor a ser pago por um produto, cosiderando o seu 
preço normal e condições de pagamento:

    à vista dinheiro: 10% de desconto
    à vista no cartão: 5% de desconto
    em até 2x no cartão: preço normal
    3x ou mais no cartão: 20% juros
'''
print('='*30)
print('{:+^30}'.format(' Caixa da Loja '))
print('='*30)
print()

preco = float(input('Informe o preço do produto: '))
print('1- à vista dinheiro\n2- à vista no cartão\n3- em até 2x no cartão\n4- 3x ou mais no cartão')
pagamento = int(input('Informe a foram de Pagamento: '))
print()

if pagamento == 1:
    precoNovo = preco - (preco * 0.1)
    print('O valor do produto com desconto de "10%" é R$ {:.2f}'.format(precoNovo))
elif pagamento == 2:
    precoNovo = preco - (preco * 0.05)
    print('O valor do produto com desconto de "5%" é R$ {:.2f}'.format(precoNovo))
elif pagamento == 3:
    print('Você escolheu pagar em 2x no cartão. O valor da parcela do produto é 2 X de R$ {:.2f} '.format(preco/2))
elif pagamento == 4:
    precoNovo = preco + (preco * 0.2)
    print('Você escolheu pagar em 3x ou mais no cartão. Portanto, o valor final do produto será R$ {:.2f}'.format(precoNovo))
else:
    print('Opção invalida de pagamento. Tente Novamente!')
print()
