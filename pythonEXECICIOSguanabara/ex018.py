#faca um programa que leia um angulo e mostre na tela o valor do seno, cosseno e tangente.

'''catOpt = float(input('Qual a altura : '))
catAdj = float(input('Qual a largura :'))
hipotenusa = (catOpt**2) + (catAdj**2)
seno = catOpt / hipotenusa
cosseno = catAdj / hipotenusa
tangente = seno / cosseno'''

import math

ang = float(input('Digite o valor do angulo :'))

#Como estamos pedindo em angulos precisa converte para que o calculo seja correto por isso uma biblioteca dentro da 
# outra para a converão so calculo correto


seno = math.sin(math.radians(ang))
print(' Num angulo de {} o valor do seno é {:1f}'.format(ang,seno))
cos = math.cos(math.radians(ang))
print('o cosseno do angulo {} é {:2f}'.format(ang,cos))
tag = math.tan(math.radians(ang))
print('E a tangente é {:2f}'.format(tag,int(tag)))

