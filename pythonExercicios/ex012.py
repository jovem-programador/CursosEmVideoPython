n1 = float(input('Qual é o preço do produto: R$'))
promocao = n1 - ((n1 * 5) / 100)
print('Valor do produto: {:.2f}, na promoção de 5%. Vai custar R${:.2f}'.format(n1, promocao))
