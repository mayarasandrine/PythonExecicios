preco = float(input('Qual o valor atual do produto ?'))
acrescimo = 0.10
novovalor = preco * (1 - acrescimo)
print('o novo valor do produto é ${:.2f}'.format(novovalor))
# poderia ser assim também
print('o valor do produto é {} com o desconto ficará {:.2f}'.format(preco,novovalor))
#para calcucamos a porcentagem podemos realizar a simples conta abaixo.
# vamos solicitar um numero , exemplo : 500 para que eu possa saber quanto é 22% desse valor
#precismos apenas fazer: 500*22/100

