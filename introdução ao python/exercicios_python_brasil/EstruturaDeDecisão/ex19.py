'''
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com:
 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
 '''
num = 0

while num < 1 or num > 1000:

    num = int(input('Digite um numero entre 1 e 1000: '))

num = str(num)


lista_numeros = []

i = 0
for elemento in num:
    lista_numeros.append(int(num[i]))
    i += 1


if len(lista_numeros) == 4:
    if lista_numeros[1] > 1 or lista_numeros[1] == 0 :
        centena = 'centenas'
    else:
        centena = 'centena'
    if lista_numeros[2] > 1 or lista_numeros[2] == 0:
        dezena = 'dezenas'
    else:
        dezena = 'dezena'
    if lista_numeros[2] > 1 or lista_numeros[2] == 0:
        unidade = 'unidades'
    else:
        unidade = 'unidade'
    print(f'{num} = {lista_numeros[0]} milhar, {lista_numeros[1]} {centena}, {lista_numeros[2]} {dezena} e {lista_numeros[1]} {unidade}.')


if len(lista_numeros) == 3:
    if lista_numeros[0] > 1 or lista_numeros[0] == 0:
        centena = 'centenas'
    else:
        centena = 'centena'
    if lista_numeros[1] > 1 or lista_numeros[1] == 0:
        dezena = 'dezenas'
    else:
        dezena = 'dezena'
    if lista_numeros[2] > 1 or lista_numeros[2] == 0:
        unidade = 'unidades'
    else:
        unidade = 'unidade'

    print(f'{num} = {lista_numeros[0]} {centena}, {lista_numeros[1]} {dezena}, e {lista_numeros[2]} {unidade}.')

if len(lista_numeros) == 2:
    if lista_numeros[0] > 1 or lista_numeros[0] == 0:
        dezena = 'dezenas'
    else:
        dezena = 'dezena'
    if lista_numeros[1] > 1 or lista_numeros[1] == 0:
        unidade = 'unidades'
    else:
        unidade = 'unidade'

    print(f'{num} = {lista_numeros[0]} {dezena}, e {lista_numeros[1]} {unidade}.')

if len(lista_numeros) == 1:
    if lista_numeros[0] > 1 or lista_numeros[0] == 0:
        unidade = 'unidades'
    else:
        unidade = 'unidade'

    print(f'{num} = {lista_numeros[0]} {unidade}.')
