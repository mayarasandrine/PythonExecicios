numero = int(input("digite um numero ?"))
'''n1 = numero * 1
n2 = numero * 2
n3 = numero * 3
n4 = numero * 4
n5 = numero * 5
n6 = numero * 6
n7 = numero * 7
n8 = numero * 8
n9 = numero * 9
n10 = numero * 10'''
# para comentar um bloco é preciso apenas coloca 3 x ' no comeco e no final do bloco desejado.
print('o numero informado é {}'.format(numero))
#podemos resolver esse codigo assim um pouco mais extenso com variavel ou podemos fazer diretamente no codigo
#print('Sua tabuada é sua tabuada é,\n numero * 2 = {} \n numero *  3 = {},\n numero * 4 = {},'
      #'\n numero * 5 = {},\n numero * 6 = {},\n numero * 7 = {},\n numero * 8 = {},\n numero * 9 = {},'
      #'\n numero * 10 = {},\n'.format(n2,n3,n4,n5,n6,n7,n8,n9,n10),end=' ')
# segunda forma de execulta esse codigo
print('___________')
print('{} x {} = {:2}'.format(numero, 1,numero*1))
print('{} x {} = {:2}'.format(numero, 2,numero*2))
print('{} x {} = {:2}'.format(numero, 3, numero*3))
print('{} x {} = {:2}'.format(numero, 4,numero*4))
print('{} x {} = {:2}'.format(numero, 5,numero*5))
print('{} x {} = {:2}'.format(numero,6,numero*6))
print('{} x {} = {:2}'.format(numero,7,numero*7))
print('{} x {} = {:2}'.format(numero,8,numero*8))
print('{} x {} = {:2}'.format(numero,9,numero*9))
print('{} x {} = {}'.format(numero,10,numero*10))
print('___________')

