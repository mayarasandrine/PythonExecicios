km = float(input('Qual a km percorrida ?'))
dias = int(input('Quantos dias foi alugado o veiculo?'))
dia = 60 * dias
kmR = 0.15 * km
# podemos também fazer essa conta da seguinte maneira
#pago = (dias * 60) + (km * 0.15)
pago = (dias * 60) + (km * 0.15)
totaldiaria = dia + kmR
print('a Km percorrida foi de {} em {} dias'.format(km,dias))
print('Total do custo com o aluguel será {} '.format(totaldiaria))
print('Total a pagar é {}'.format(pago))
# das duas forma de calculo o retorno é o mesmo


