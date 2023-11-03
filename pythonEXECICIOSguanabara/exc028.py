''''Escreva um programa que faca o computador pensar em um numero inteiro
entre 0 e 5 e peça para o usuario tentar descobri qual foi o numero escolhido pelo
computador.
o programa devera escreve na tela se o usuario vendeu ou perdeu'''

import random  # estou importando uma biblioteca

from time import sleep
n = random.randint(0,5) # criei um aleatorio
print('*' * 50) # apenas para deixa a interface bonitinha

print('pensei em um numero entre 1 a 5 tente adivinha')

print('*' * 50)
nusuario = int(input("Em que numero eu pensei querido(a)? "))
print('processando....')
sleep(2) # quero dizer que nessa parte do programa ele vai demorar um pouco pensando
if nusuario == n:
    print("voce venceu")
    print("*" * 50)
else:
    print('*'*50)
    print(f"voce perdeu, hahaha pensei em {n} e não em {nusuario}")
