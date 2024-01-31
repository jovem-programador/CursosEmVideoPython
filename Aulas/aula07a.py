# Alinhamento de String
#nome = input('Digite seu nome: ')
#print('Prazer em conhecer !{:20}!'.format(nome))
#print('Prazer em conhecer !{:^20}!'.format(nome))
#print('Prazer em conhecer !{:>20}!'.format(nome))
#print('Prazer em conhecer !{:<20}!'.format(nome))
#print('Prazer em conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print(f'A soma vale: {n1 + n2}', end=' ') #Juntando com end prints
print(f'A multiplicação vale: {n1 * n2}')
print(f'A expodenciação vale: {n1 ** n2}')
print('A divisão vale: {:.2f}'.format(n1 / n2)) #Formatando valor flutuante
print(f'A divisão inteira vale: {n1 // n2}')
print(f'O resto da divisão vale: {n1 ** n2}')
#Quebrar linha em Python: \n
