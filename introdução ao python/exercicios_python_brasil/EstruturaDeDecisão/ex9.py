'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

num_1 = float(input('Digite o primeiro numero: '))
num_2 = float(input('Digite o segundo numero: '))
num_3 = float(input('Digite o terceiro numero: '))

numbers_list = []

numbers_list.append(num_1)

numbers_list.append(num_2)

numbers_list.append(num_3)

numbers_list.sort(reverse=True)

i = 0

for x in numbers_list:
    print(numbers_list[i])
    i += 1
