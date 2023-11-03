'''Crie um programa que leia um nome de uma pessoa e diga se tem silva'''

n = str(input("digite o seu nome completo:")).strip()
e = 'silva' in n
print('seu nome tem silva ? {}'.format(e))

'''outra forma de declarar esse encontro é na propria chamada'''
print('Tem silva no seu nome ? {}'.format('silva' in n.upper()))
#lembra sempre de declarar como queremos que seja encontrada essa varivael 
