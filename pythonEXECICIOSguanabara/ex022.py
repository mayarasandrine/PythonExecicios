'''crie um progroma que leia o nome completo de uma pessoa e mostre
: o nome com toda as letras maiuculas
:o nome com todas as letras minusculas
: quantas letras ao todo sem considerar o espaço
: quantas letra tem o primeiro nome'''


nome = str(input("qual o seu nome completo:")).strip()
# quando colocamos um strip no começo eu quero dizer que ja quero que ele retire os espaço inutel da pergunta


print("Vamos analisar seu nome abaixo:")
#upper coloca toda a string em maiusculo
print("seu nome Maiusculo é {}".format(nome.upper()))
print("seu nome em Minusculo é {}".format(nome.lower()))
print("seu nome tem {} letras".format(len(nome) - nome.count(' ')))
#eu pedi para o programa contar quantas letras tem e fiz um count para ele retirar o espaco nessa contagem

separa = nome.split()
print("seu primeiro nome é {} e tem {} letras".format(separa[0], len(separa[0])))



