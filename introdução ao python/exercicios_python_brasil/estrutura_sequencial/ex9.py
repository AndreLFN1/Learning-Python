'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).

'''

temperatura_F = float(input('Qual a temperatura atual em Fahrenheit? '))

temperatura_C = 5*((temperatura_F-32)/9)

print(f'A temperatura dada em Farenheit ({temperatura_F}) é igual à {temperatura_C} graus Celcius')
