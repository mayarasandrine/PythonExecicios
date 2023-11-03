carteira = float(input("quanto voce tem em dinheiro?"))
Real = 1
Dollar = 5.05
SaldoConvertido = Real * (carteira / Dollar)
print('seu saldo atualmente é ${} em Dollar voce teria ${:.2f}'.format(carteira,SaldoConvertido))




