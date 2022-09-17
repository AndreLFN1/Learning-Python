'''

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.

'''

print('Bem vindo à cores belas tinturaria!\n')

area = int(input('Qual a medida em metros quadrados da área a ser pintada? '))

#é necessário dividir os metros quadrados em 3 para saber o
#numero de latas no entanto, precisamos arredondar esse
#numero para cima, porque não podemos permitir a compra
#de frações de latas de tinta

litros_de_tinta = area//6
folga = litros_de_tinta*1.1
#com os litros em mãos, o programa calcula o numero de
#latas de tinta, também em numeros inteiros

quantidade_de_latas = litros_de_tinta//18
quantidade_de_galões = litros_de_tinta//3.6

#agora é só multiplicarmos pelo valor de cada lata de titna

preço_a_ser_pago_latas = quantidade_de_latas*80
preço_a_ser_pago_galões = quantidade_de_galões*25
#e o restante é só informar os valores para o usuário
#caso o numero de latas de tinta seja menor do que 1, é importante definir que o usuário compre apenas uma

print('COMPRANDO APENAS LATAS')

if quantidade_de_latas >= 1:
    print(f'Muito bem, o número total de latas necessário será {quantidade_de_latas} e o valor será de R${preço_a_ser_pago_latas}')
else:
    print('Muito bem, o número total de latas necessário será 1 e o valor será de R$80,00')

print('*'*100)

print('COMPRANDO APENAS GALÕES')

if quantidade_de_galões >= 1:
    print(f'Muito bem, o número total de latas necessário será {quantidade_de_galões} e o valor será de R${preço_a_ser_pago_galões}')
else:
    print('Muito bem, o número total de galões necessário será 1 e o valor será de R$25,00')

print('*'*100)

print('COMPRANDO LATAS E GALÕES')

#minha ideia aqui é definir tudo com ifs e elifs

#esse primeiro vai definir a quantidade de tinta com folga

quantidade_de_latas = folga//18
quantidade_de_galões = folga//3.6


if quantidade_de_latas <= 1:
    quantidade_de_galões = litros_de_tinta//3.6 + 1
    print(f'Não há necessidade de comprar latas de tinta, apenas {quantidade_de_galões} galões! ')
