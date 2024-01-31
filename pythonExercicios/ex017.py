import math
a = float(input('Informe o Cateto Oposto: '))
b = float(input('Informe o Cateto Adjacente: '))
hyportenusa = math.hypot(a, b)
print('{:.2f}'.format(hyportenusa))
