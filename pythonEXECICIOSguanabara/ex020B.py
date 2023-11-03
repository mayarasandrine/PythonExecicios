import random

n1 = str(input('digite o primeiro nome: '))
n2 = str(input('digite o segundo nome: '))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome: '))

#alunos = (n1,n2,n3,n4)
#ordem = random.sample(alunos, len(alunos))
''' o sample faz com que ele tire o numero soteado e continue com o restante sem repetir no codigo ou 
pode ser feita com a shuffle , que quer dizer enbaralhar'''


lista = [n1,n2,n3,n4] #cuidado nos fechamentos da sitaxe por que as vezes o () dar erro devido a nao ser o correto para a expressao

random.shuffle(lista)
print("a ordem sera")
print(lista)
#print(" a ordem de apresentação será {}, {}, {}, {} ".format(ordem[0],ordem[1],ordem[2],ordem[3]))