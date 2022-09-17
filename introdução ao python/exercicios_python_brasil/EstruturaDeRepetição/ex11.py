'''
Altere o programa anterior para mostrar no final a soma dos números
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

soma_numeros = num_1 + num_2
print(f'A soma dos numeros é {soma_numeros}')
