''' faca um programa  que sortei qual aluno vai apagar o quadro'''

import random

n1 = str(input(" Qual o nome do primeiro aluno : "))
n2 = str(input("Qual o nome do segundo aluno : "))
n3 = str(input('Qual o nome do terceiro aluno : '))
n4 = str(input('Qual o nome do quarto aluno : '))

alunos = (n1,n2,n3,n4)
sorteado = random.choice(alunos)

print("O aluno que vai apagar o quadro é {}".format(sorteado))
