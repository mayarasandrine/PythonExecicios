# como so usamos uma ou mais especifica do metodo, vamos especificar
'''PRIMEIRO MEDOTO DE REALIAZR O PROGRAMA
nomes o numero qualquer e sua parte inteira'''

import math
from math import floor,trunc
n = float(input('digite um numero:'))
print('o numero é {} e sua parte inteira é {}'.format(n,floor(n)))
# ele destrinxou a parte inteira do numero ou pode ser feito
print('o numero informado foi {} e sua porção inteira {}'.format(n,trunc(n)))
# esse medoto trunc ele corta a parte inteira do numero

# COM ISSO TAMBÉM PRECISAMOS RETIRAR O MATH DAS EXPLICAÇÃO conforme exemplo'''


'''EXEMPLO
print('o numero informado é {} e sua parte inteira è {}'.format(n,math.trunc(n))) seria dessa forma se tivemos
 utilizando o metodo gerenico de vez de especificar'''

#segundo metodo de como realizar o programa
n = float(input('Digite um numero qualquer:'))
print('o valor informado foi {} e sua porção inteira é {}'.format(n,int(n)))



