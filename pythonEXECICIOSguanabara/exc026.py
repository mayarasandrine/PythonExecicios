'''crie um programa que leia uma frase pelo o teclado e mostre
°quantas vezes aparecer a letra A
° em que posicição ela aparece a primeira vez
° em que posição ela aparece pela ultima vez '''

f = str(input("digite uma frase:")).strip().lower()

print("A Letra A aparece {} vezes na frase".format(f.count("a")))
print("A Primeira vez que a letra a apareceu na posição {}".format(f.find("a")))
# ai o programa vai começa a conta do 1 e nao do 0
print(" A ultima vez que a letra A apareceu na posição {}".format(f.rfind('a')))

