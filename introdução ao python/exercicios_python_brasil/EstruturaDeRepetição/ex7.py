'''
Faça um programa que leia 5 números e informe o maior número.
'''


num = int(input('Digite o numero 1: '))

i = 2
while i < 6:
    num_2 = int(input(f'Digite o numero {i}: '))
    if num_2 > num:
        num = num_2
    else:
        num = num
    i += 1

print(f'O maior numero digitado foi: {num}')
