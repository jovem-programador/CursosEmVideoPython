num = int(input('Digite um número: '))

u = num // 1 % 10
b = num // 10 % 10
c = num // 100 % 10
d = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {b}')
print(f'Centena: {c}')
print(f'Milhar: {d}')
