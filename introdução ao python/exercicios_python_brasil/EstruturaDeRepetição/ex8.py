'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

i = 1
soma = 0
while i <= 5:
    num = int(input(f'Digite o numero {i}: '))
    soma += num
    i += 1

print(soma)
