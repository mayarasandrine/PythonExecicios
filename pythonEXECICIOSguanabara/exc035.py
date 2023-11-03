'''crie um programa que leia o comprimento de tres retas e diga ao usuarios se elas
podem ou nao forma um trinagulo '''

from time import sleep
print('\033[1;30;43mBem vindo a sua analise!\033[m') # faz com que tenha cor porem nao fica até o fim e alem
print('-='*12)
print('\033[1;34;40mANALISANDO TRINAGULOS \033[m')
print('-='*12)
l1 = float(input('\033[4mprimeiro seguimento: ? \033[m'))
l2 = float(input('segundo seguimento:  ? '))
l3 = float(input('terceiro seguimento: ? '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("os seguimentos acima podem forma um TRIANGULO")
else:
    print("os seguimetos acima não podem forma um triangulo ")


