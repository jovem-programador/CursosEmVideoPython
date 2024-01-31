# Manipulando Cadeias De Textos
frase = 'Curso em Video Python'
print(frase)

# Fateando
print(frase[::2])

# Analise
print(frase.count('o'))
print(len(frase))
print('Curso' in frase)
print(frase.find('Curso'))

# Transformação
print(frase.strip())
print(frase.replace('Curso', 'Aula'))

# Divisão
dividido = frase.split()
print(dividido)

# Junção
print('.'.join(dividido))
