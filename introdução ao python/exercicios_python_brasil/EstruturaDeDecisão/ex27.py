'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo
para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
escreva o valor a ser pago pelo cliente.
'''

peso_morango = float(input('Quantos Kg de morango você deseja comprar? '))

peso_maca = float(input('Quantos Kg de maçã você deseja comprar? '))

peso_total = peso_morango + peso_maca

if peso_morango > 0:

    if peso_morango <= 5:
        valor_morango = peso_morango*2.50
    elif peso_morango > 5:
        valor_morango = peso_morango*2.20

if peso_maca > 0:

    if peso_maca <= 5:
        valor_maca = peso_maca*1.80
    elif peso_maca > 5:
        valor_maca = peso_maca*1.50

valor_a_ser_pago = valor_maca + valor_morango

if peso_total > 8 or (valor_maca + valor_morango) > 25:

    valor_a_ser_pago = valor_a_ser_pago*0.90


print(f'O valor a ser pago é de R${valor_a_ser_pago}')
