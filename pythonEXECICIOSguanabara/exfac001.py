
'''crie um programa que leia a nota do aluno e mostre na tela o status que ele se encontra no escola
e caso a nota informada nao seja entre 1 a 10 '''


aluno = int(input('digite sua nota:'))


if aluno <= 4:
    print("voce está reprovado ",aluno)
elif aluno <= 6:
       print("voce se encontra em recuperação",aluno)
elif aluno <=10:
    print("parabens, voce está aprovado",aluno)
else:
    print("nota invalida")
