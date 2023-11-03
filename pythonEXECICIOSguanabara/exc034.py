'''escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu
aumento. para salarios superior a R$1250, calcule um aumento de 10%
para salarios inferior calcule 15%'''

#primeira forma de como resolver a questão

s = float(input("\033[7;32;40mqual o seu salario atual ? RS: "))
aumento15 = s *(15/100)
aumento10 = s *(10/100)
if s > 1250:
    print(f"\033[7;32;40mseu salario atual é R${s}\n"
          f"seu salario recerá um aumento de 10% \n"
          f"sendo RS {aumento10} \n"
          f"atualizando seu salario para RS{s+aumento10}")
else:
    s <= 1250
    print(f'\033[1;32;40mvoce recebará um aumento de 15% \n '
          f'sendo R% {aumento15} \n'
          f'o novo salario ficará RS {s+aumento15}')



