'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
'''

#achei uma função chamada isinstance ela checa o tipo de variável

numero = float(input('Digite um numero inteiro ou um numero float! '))


if (numero - numero//1) == 0:
    print('Este é um numero inteiro!')
else:
    print('Este é um numero float!')
