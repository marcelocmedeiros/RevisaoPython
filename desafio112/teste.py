import dado as dado

from desafio112.utilidades import moeda
from desafio112.utilidades import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 20, 12)