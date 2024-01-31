print('\033[1;30;47m Teste \033[m')

nome = 'Marley'
print('Prazer em conhecer {}{}{}'.format('\033[1;35m', nome, '\033[m'))


cores = {
    'limpa': '\033[m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[1;31m',
}

print('Prazer em conhecer {}{}{}'.format(cores['vermelho'], nome, cores['limpa']))
print(19 // 2)
print(len('prova de python'))
