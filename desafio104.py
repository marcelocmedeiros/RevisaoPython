# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 21 Funções (Def) 2° parte---> GUSTAVO GUANABARA

'''
Faça um Programa que tenha uma função leiaInt() que vai funcionar semelhante à função input() do Python
só que fazendo a valiação par aceitar apenas um valor numérico. ex: n = leiaInt
'''

print('='*30)
print('{:*^30}'.format(' Def leiaInt() '))
print('='*30)
print()

# função leiaInt() vai receber um valor q tem ser numérico
def leiaInt(msg):
    """-> recebe um número

    Arguments:
       msg = recebe uma msg (str)

    Returns:
        retorna um número int
    """
    # variável ok = False para inicial avalização
    ok = False
    valor = 0
    # loop infinito para só para quando for colocado um número
    while True:
        # variável n = msg
        n = str(input(msg))
        # se n = número  (é numerico)
        if n.isnumeric():
            # valor converte n str em n int
            valor = int(n)
            # quando ok = True ele break e retorna o valor do número
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# programa principal
n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')
