#Faça um programa que peça 2 números iunteiros e um
#número float. Calcule e mostre:
#1) O produto do dobro do primeiro com metade do segundo
#2) A soma do triplo do primeiro com o terceiro
#3) O terceiro elevado ao cubo



primeiro_numero = int(input('Forneça o primeiro numero inteiro: '))
segundo_numero = int(input('Forneça o segundo numero inteiro: '))
terceiro_numero = float(input('Forneça um numero não inteiro: '))

primeira_equação = (primeiro_numero*2)*(segundo_numero/2)
segunda_equação = primeiro_numero*3 + terceiro_numero
terceira_equação = terceiro_numero**3

print(f'O produto do dobro do primeiro numero com metade do segundo é: {primeira_equação}')
print(f'A soma do triplo do primeiro número com o terceiro é: {segunda_equação}')
print(f'O terceiro número elevado ao cubo é: {terceira_equação}')
