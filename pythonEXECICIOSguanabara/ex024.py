'''crie um programa que leia um nome de uma cidade e diga se existe
santo ou nao '''


c = str(input("qual a cidade que voce nasceu:")).strip()
# o strip removeu toda e qualquer espaço que possa dar erro
print(c[:5].upper() =='SANTOS')
# o upper coloca a string quando for procurar toda em maisculo para evitar erro
