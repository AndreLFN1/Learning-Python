'''
Ex. 12

Faça um programa que receba uma string com um número de ponto flutuante,
e imprima qual a parte dele que não é inteira

Ex:

n = '3.14'

resposta: 14

'''

num = float(input('Digite um número qualquer: '))

numInString = str(num)

novo = numInString.split('.')

for x in novo:
    print(x)
