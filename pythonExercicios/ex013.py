n1 = float(input('Informe seu salario: R$'))
aumento = n1 + ((n1 * 15) / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(n1, aumento))
