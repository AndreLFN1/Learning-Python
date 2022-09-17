'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a. Álcool:
b. até 20 litros, desconto de 3% por litro
c. acima de 20 litros, desconto de 5% por litro
d. Gasolina:
e. até 20 litros, desconto de 4% por litro
f. acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço
do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

'''

combustivel = input('Álcool (A) ou Gasolina (G?): ')

if combustivel == 'A':
    volume = float(input('Qual o volume de álcool? '))

    if volume <= 20:
        valor_a_ser_pago = (volume*1.90)*0.97
    elif volume > 20:
        valor_a_ser_pago = (volume*1.90)*0.95



if combustivel == 'G':

    volume = float(input('Qual o volume de gasolina? '))
    #estruturar as decisões

    if volume <= 20:
        valor_a_ser_pago = (volume*2.50)*0.96
    elif volume > 20:
        valor_a_ser_pago = (volume*2.50)*0.94

print(f'O valor a ser pago é de R${valor_a_ser_pago}! ')
