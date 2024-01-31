import math
an = float(input('Digite o ângulo que você deseja: '))

# Convertendo para Radianos
angulo = math.radians(an)

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('Ângulo: {}, Seno: {:.2f}, Cosseno: {:.2f}, Tangente: {:.2f}'.format(an, seno, cosseno, tangente))
