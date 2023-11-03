'''Crie um programa que leia um numero de 1 a 9999 e mostre na tela cada um dos digitos
separados
unidade
dezena
centena
e milhar'''

numero = int(input("digite um numero :"))
qtd = 1 and 999
u = numero//1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print("analisando o numero {}".format(numero))
print("unidade: {}".format(u))
print("dezena: {}".format(d))
print("centena: {}".format(c))
print('Milhar: {}'.format(m))

