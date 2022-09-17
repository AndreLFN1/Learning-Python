'''
Faça um Programa que converta metros para centímetros.
'''

def conversor_metros_centimetros(metros):
    centímetros = metros*100
    return centímetros



medida = float(input('Digite quantos metros você deseja converter para centímetros: '))

print(f' A conversão de {medida} metros para centímetros é: {conversor_metros_centimetros(medida)}')
