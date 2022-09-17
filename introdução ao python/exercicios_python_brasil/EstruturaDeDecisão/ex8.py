'''
Faça um Programa que leia três números e mostre o maior deles.

'''

num_1 = float(input('Qual o valor do primeiro produto? '))
num_2 = float(input('Qual o valor do segundo produto? '))
num_3 = float(input('Qual o valor do terceiro produto? '))

if num_1 < num_2 and num_1 < num_3:
    print(f'Você deve comprar o primeiro produto!!')

if num_2 < num_1 and num_2 < num_3:
    print(f'Você deve comprar o segundo produto!!')

if num_3 < num_1 and num_3 < num_2:
    print(f'Você deve comprar o terceiro produto!!')
