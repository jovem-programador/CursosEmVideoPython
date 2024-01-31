from datetime import date
dataAtual = date.today()
anoAtual = dataAtual.year

a = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))


def bissexto(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print(f'O ano {a} é BISSEXTO')
    else:
        print(f'O ano {a} NÃO é BISSEXTO')


if a == 0:
    bissexto(anoAtual)
else:
    bissexto(a)
