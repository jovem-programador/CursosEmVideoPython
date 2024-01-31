d = int(input('Qual é a distância da sua viagem? '))
v1 = 0.50
v2 = 0.45

if d <= 200:
    t = d * v1
    print('Você está prester a começar uma viagem de {:.1f}Km.'.format(d))
    print('E o preço da sua passagem será de R${:.2f}'.format(t))
else:
    t = d * v2
    print('Você está prester a começar uma viagem de {:.1f}Km.'.format(d))
    print('E o preço da sua passagem será de R${:.2f}'.format(t))
