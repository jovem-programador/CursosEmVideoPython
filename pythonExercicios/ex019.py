import random

al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))

# Lista em Python
lista = [al1, al2, al3, al4]

#aleatorio = random.randint(0, 3)
escolhido = random.choice(lista)

print('Aluno escolhido foi: {}'.format(escolhido))

'''
if aleatorio == 1:
    print(f'Aluno escolhido: {al1}')
elif aleatorio == 2:
    print(f'Aluno escolhido: {al2}')
elif aleatorio == 3:
    print(f'Aluno escolhido: {al3}')
elif aleatorio == 4:
    print(f'Aluno escolhido: {al4}')
'''