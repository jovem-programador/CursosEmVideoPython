salario = float(input('Qual é o salario do funcionario: '))

taxa01 = 0.15
taxa02 = 0.10

if salario > 1250.00:
    novoSalario = (salario * taxa02) + salario
    print('Quem ganhava R${:.2f}. Passa a ganhar R${:.2f}!'.format(salario, novoSalario))
else:
    novoSalario = (salario * taxa01) + salario
    print('Quem ganhava R${:.2f}. Passa a ganhar R${:.2f}!'.format(salario, novoSalario))
