'''escreva um programa que leia a velocidade do veiculos:
se ele ultrapassar 80km/h ,mostre uma mensagem dizendo que ele foi multado
a multa vai custa RS7,00 por cada Km acim do limite'''
from time import sleep


velocidade = float(input('Qual foi a KM ultrapassada:'))
limite = 80
multa = 7

if velocidade > limite:
    kmUltrapassada = velocidade - limite
    Valormultra = multa * kmUltrapassada
    print("PROCESSANDO...")
    sleep(2)
    print('*'*29)
    print(f'Voce foi multado em R${Valormultra} ')

else:
    print("Tenha um bom dia, no Transito escolha a vida")
    print("*"*45)
