temperatura = float(input('Informe qual a temperatura em °C:'))
#essa é uma formula para a conversão ja declarada na variante
f=(9 * temperatura)/5 +32
# ou podemos fazer F=(temperatura*9/5)+32 da o mesmo resultado
print('A temperatura atual é {} convertida para °F fica {}'.format(temperatura,f))
#também podemos usar a ordem de precedencia que seria: f = 9 * temperatura / 5 + 32 sem precisa os parenteses


