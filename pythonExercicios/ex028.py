# Joginho em Python
from time import sleep
from random import randint

# Número aleatorio
n = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

sleep(2)

print('PROCESSANDO...')

sleep(2)

a = int(input('Em que número eu pensei? '))

sleep(2)

if n == a:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {n} e não no {a}!')
