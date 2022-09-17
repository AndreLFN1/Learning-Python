'''
Faça um Programa que leia três números e mostre o maior deles.

'''

num_1 = float(input('Digite o primeiro numero: '))
num_2 = float(input('Digite o segundo numero: '))
num_3 = float(input('Digite o terceiro numero: '))

if num_1 > num_2 and num_1 > num_3:
    print(f'O maior numero é: {num_1}')

if num_2 > num_1 and num_2 > num_3:
    print(f'O maior numero é: {num_2}')

if num_3 > num_1 and num_3 > num_2:
    print(f'O maior numero é: {num_3}')
