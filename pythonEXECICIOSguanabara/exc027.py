'''faca um programa que leia o nome completo da pessoa e mostre o primeiro e ultimo nome'''

n = str(input("digite seu nome completo:")).strip().upper()
s = n.split()
print('um prazer em lhe conhecer !'
      f'seu primeiro nome é {s[0]} \n'
      f'Seu ultimo nome é {s[-1]}')
