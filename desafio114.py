# Marcelo Campos de Medeiros
# ADS UNIFIP
# REVISÃO DE PYTHON
# AULA 23 Tratamento de Erros---> GUSTAVO GUANABARA

'''
Crie um código em Python que teste se o site pudim está acessível pelo usuário
'''

print('='*40)
print('{:*^30}'.format(' Teste o site pudim' ))
print('='*40)
print()

# importe esta bilioteca para verificar a url do site
import urllib
import urllib.request

# tratamento de excesão try
try:
    # o site = http://www.pudim.com.br / mas pode ser qualquer um 
    site = urllib.request.urlopen('http://www.pudim.com.br')
    # tipo de excesão
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento!')
else:
    print('Cosegui acessar o site Pudum com sucesso!')