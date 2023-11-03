'''crie um programa que pergunte a distancia de uma viagem em
km.
° calcule o preço da passagem, cobrado R$0,50 por km
para viagens de até 200km e R$0,45 para viagens mais
longas '''

'''Primeira maneira de realizar o programa'''
from time import sleep

distancia = float(input("\033[1;33;40mQual a distancia da viagem? "))
pbarata = distancia * 0.50
pcara = distancia * 0.45
print("\033[1;32;40mCARREGANDO...")
sleep(1)
if distancia <= 200:
    print(' - ' * 20)
    print(f'\033[1;33;40m Você está preste a ir para uma viagem de {distancia}km \n'
          f'o valor da passagem será R${pbarata} reais')
else:
    print(' - '*20)
    print(f'Você está presta a viajar {distancia} km\n'
          f'O valor da passagem é R${pcara} reais')

#segunda opção de como realizar o programa

from time import sleep
d = float(input('\033[1;33;40mQual a distancia da sua viagem?'))# adicieni algumas cores apenas para dar uma colorida
print(f'Voce está preste e viajar {d} km')
preco = d * 0.50 if d <= 200 else d * 0.45
print("\033[1;34;40mCARREGANDO...")
sleep(1)
print(f"o preço da sua passagem é R${preco} \n "
      "Boa viagem e volte sempre")

