n1 = float(input('Largura da parede: '))
n2 = float(input('Altura da parede: '))
area = n1 * n2
print('Sua parede tem a dimensão de {:.2f}x{:.2f}. Sua área é de {:.2f}m2'.format(n1, n2, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(area / 2))
