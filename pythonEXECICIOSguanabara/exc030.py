''''crie um programa que leia um numero inteiro e mostre na tela se ele é
par ou impar'''


n = int(input('digite um numero: '))
resultado = n % 2 #todo numero par o resto vai ser 1
# todo numero numero impar o resto vai ser 0
if resultado == 0:
    print(f'o numero {n} é PAR')
    print(' * '*10)
else:
    print (f'o numero {n} é IMPAR')
    print(' * '*10)
