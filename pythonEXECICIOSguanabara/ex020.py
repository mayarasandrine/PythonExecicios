import random

alunos = ['mayara','sandrine','lorena','dayane']
random.shuffle(alunos)

print('A Ordem de apresentação é')
for i, alunos in enumerate(alunos,start=1):
 print('a ordem é {} {}'.format(i,alunos))
