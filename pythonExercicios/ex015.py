d = int(input('Quantos dias o carro alugados? '))
km = float(input('Quantos Km rodados? '))
valor = (d * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(valor))
