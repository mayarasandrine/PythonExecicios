'''crie um programa que leia o ano e mostre se ele é bixesto
se eu quiser que o programa possa ler a data do computador e me dizer se o ano
atual é '''

from datetime import date

ano = int(input("Que ano deseja analisar ? digite 0 para analisar o ano atual: "))
if ano ==0:
    ano = date.today().year # essa instrução faz com ele o programa pegue o ano atual que está sendo rodado.

if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0: # formula para mostra se o ano é bissexto
    print(f"o ano {ano} É BISSEXTO ")
else:
    print(f'o ano {ano} NÃO É BISSEXTO')