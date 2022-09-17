'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

temperatura_C = float(input('Qual a temperatura atual em Celcius? '))

temperatura_F = 9*temperatura_C/5 + 32

print(f'A temperatura dada em Celcius ({temperatura_C}) é igual à {temperatura_F} graus Farenheit')
