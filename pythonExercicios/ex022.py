nome = str(input('Digite seu nome completo: ')).strip()
divisao = nome.split()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome é {divisao[0]} e ele tem {len(divisao[0])} letras')
