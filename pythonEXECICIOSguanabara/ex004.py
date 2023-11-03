##N1 = int(input('informe o primeiro numero que veio a sua mente:'))
#N2 = int(input('Agora qual o segundo numero que você pensou?'))
##S = N1+N2
##print('Então o primeiro numero que você pensou é {} é o segundo {} que resulta na soma {}'.format(N1,N2,S)


# outro medoto de como esse execicio pode ser execultado
#o input sempre vai retorno que é uma stir por ser o tipo do primitivo
a = input('Digite algo?')
print('o tipo primitivo desse valor é', type(a))
#aqui conseguimos saber se é numerico
print('é um valor numerico?',a.isnumeric())
#quando eu quero saber se tem espaco nessa vaviavel declarada
print('tem espaco na variavel?',a.isspace())
print('é um numero decimal? ', a.isdecimal())
# para saber se é alfabetico
print('é alfabetico ?', a.isalpha())
# para saber se é alfanumerico
print('é alfanumerico', a.isalnum())
# para sabemos se está em maiusculas
print('está em maiusculas ?', a.isupper())
# para sabemos se está em minusculas
print('está em minusculos ?',a.islower())
#para saber se a palavra está capitalizada
print('está capitalizada', a.istitle())