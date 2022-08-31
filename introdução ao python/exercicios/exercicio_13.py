'''
Ex. 13

Faça um programa que: Dada uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e um número
inteiro, imprima a tabuada desse número



multiplicadores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero_dado = int(input('Digite um número para obter a sua tabuada: '))

i = 0

while i < 11:
    print(multiplicadores[i]*numero_dado)
    i += 1

OBS: Essa é a forma como eu resolvi, mas utilizando o for ficaria assim:
'''

multiplicadores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_dado = int(input('Digite um número para obter a sua tabuada: '))

for x in multiplicadores:
    print(x*numero_dado)
