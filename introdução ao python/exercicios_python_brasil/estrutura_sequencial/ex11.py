'''

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.

'''
#inputs

primeiro_inteiro = int(input('Digite um número inteiro: '))

segundo_inteiro = int(input('Digite outro número inteiro: '))

numero_real = float(input('Digite um numero real: '))



#outputs

# produto do dobro do primeiro com metade do segundo
resultado_1 = (primeiro_inteiro*2)*segundo_inteiro/2
#soma do triplo do primeiro com o terceiro
resultado_2 = primeiro_inteiro*3 + numero_real
#o terceiro elevado ao cubo
resultado_3 =  numero_real**3

print(f'O produto do dobro do primeiro com metade do segundo é: {resultado_1}')
print(f'A soma do triplo do primeiro com o terceiro é: {resultado_2}')
print(f'O terceiro número elevado ao cubo é: {resultado_3}')
