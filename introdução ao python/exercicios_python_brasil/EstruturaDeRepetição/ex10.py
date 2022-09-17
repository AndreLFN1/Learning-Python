'''
Faça um programa que receba dois números inteiros e gere os números inteiros que
estão no intervalo compreendido por eles.
'''

num_1 = int(input('Digite o primeiro numero inteiro: '))

num_2 = int(input('Digite o segundo numero inteiro: '))


if num_1 < num_2:
    i = num_1 + 1
    while i < num_2:
        print(i, end=' ')
        i += 1

elif num_2 < num_1:
    i = num_2 + 1
    while i < num_1:
        print(i, end=' ')
        i += 1
