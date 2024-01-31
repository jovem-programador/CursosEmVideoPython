from time import sleep

v = int(input('Qual a velocidade atual do carro? '))
vm = 80
m = 7.00

sleep(1)

if v > vm:
    e = v - vm
    t = e * m
    print(f'MULTADO! Você excedeu o limite permitido que é de {vm}km/h')
    sleep(1)
    print('Você deve pagar uma multa de R${:.2f}!'.format(t))

print('Tenha um bom dia! Dirija com segurança!')
