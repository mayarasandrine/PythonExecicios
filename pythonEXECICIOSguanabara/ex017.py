'''faca um programa que leia o cateto oposto, o cateto adjacente , mostre sua hipotenusa '''


import math
catOpos = float(input('Qual o comprimento do cateto oposto ?'))
catAdj = float(input('Qual o comprimento do cateto adjacente?'))

hi = (catOpos ** 2 + catAdj ** 2) ** (1/2)

'''Primeira forma de calcular o programa acima sem usar uma biblioteca '''

print(' a hipotenusa é {:2f}'.format(hi))
#hipotenusa = math.sqrt(catAdj**2 + catOpos**2)
#print(' O cateto posto é {} e o seu adjacente {} \n '
      #'sendo assim sua hipotenusa é {} '.format(catAdj,catOpos,hipotenusa))
'''Segunda forma de calcular o programa abaixo usando a biblioteca especifica'''

#hipotenusa = math.sqrt(catAdj**2 + catOpos**2)
print('O cateto oposto é {} o seu adjacente {} '.format(catOpos,catAdj))
print(' A hipotenusa é {}'.format(math.sqrt(catAdj**2 + catOpos**2)))
#print("A hipotenusa é:", hipotenusa)

'''Terceira forma de calcular a hipotenusa com a biblioteca'''

#essa forma é mais direta por ja usar uma biblioteca especifica
hip = math.hypot(catOpos,catAdj)
print("a hipotenusa é {:.2f} ".format(hip))
