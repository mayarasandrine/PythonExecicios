numero1 = int(input('informe o primeiro numero ?'))
numero2 = int(input('informe por favor o segundo numero?'))
# mesmo eu declarando uma variavel para guardar o numero o programa entende como se fosse
#uma string por isso ela nao soma e sim junta os numeros informados.

Soma = numero1 + numero2

print(' A soma dos numero são',Soma)

## um outro exemplo de soma para deixa o codigo mais limpo seria
# print(' a soma dos numeros são {} '. format(Soma))
# o format é um comando que vamos coloca dentro dos {} o que queremos subistituir
