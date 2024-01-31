#Desafio 01
n1 = int(input('Informe um número inteiro: '))
print(f'Número: {n1}, Antecessor: {n1 - 1}, Sucessor: {n1 + 1}')

#Desafio 02
n1 = int(input('Informe um número inteiro: '))
print('Número: {}, Dobro: {}, Triplo: {}, Raiz Quadrada: {:.2f}'.format(n1, n1 * 2, n1 * 3, n1 ** (1/2)))

#Desafio 03
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
print(f'A média vale: {(n1 + n2) / 2}')

#Desafio 04
n1 = int(input('Informe o metro: '))
print(f'Metros: {n1}, Centimetros: {n1 * 100}, Milimetros {n1 * 1000}')

#Desafio 05
n1 = int(input('Informe um numero: '))
print(f'1 x {n1} = {1 * n1}')
print(f'2 x {n1} = {2 * n1}')
print(f'3 x {n1} = {3 * n1}')
print(f'4 x {n1} = {4 * n1}')
print(f'5 x {n1} = {5 * n1}')
print(f'6 x {n1} = {6 * n1}')
print(f'7 x {n1} = {7 * n1}')
print(f'8 x {n1} = {8 * n1}')
print(f'9 x {n1} = {9 * n1}')
print(f'10 x {n1} = {10 * n1}')

#Desafio 06
n1 = float(input('Quanto você tem na carteira: '))
print('Você pode comprar {:.2f}'.format(n1 / 3.27))

#Desafio 07
n1 = float(input('Qual é a altura da parede em Metros: '))
n2 = float(input('Qual é a largura da parede em Metros: '))
area = n1 * n2
tinta = 2
print(f'Area da parede em Metros: {area}, Quantidade de tintas necessarias {area / tinta}')

#Desafio 08
n1 = float(input('Informe o preço: '))
desconto = (n1 * 5) / 100
print('Valor do desconto: {:.2f}'.format(n1 - desconto))

#Desafio 09
n1 = float(input('Informe seu salario: '))
aumento = (n1 * 15) / 100
print('Novo salario: {:.2f}'.format(aumento + n1))
