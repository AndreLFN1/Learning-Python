'''Faça um Programa que peça um número correspondente a um determinado ano e em
seguida informe se este ano é ou não bissexto.

'''

ano_informado = int(input('Digite um ano para saber se o mesmo é bissexto: '))

if ano_informado%4 == 0:
    print(f'{ano_informado} é um ano bissexto!')
else:
    print('Este não é um ano bissexto!')
