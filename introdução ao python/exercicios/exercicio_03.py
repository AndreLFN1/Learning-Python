#Faça um programa para uma loja de tintas. O programa
#deverá pedir o tamanho em metros quadrados da área a ser
#pintada. Considere que a cobertura da tinta é de 1 litro
#para cada 3 metros quadrados e que a tinta é vendida em
#latas de 18 litros, que custam R$80,00. Informe ao usuário
#a quantidade de latas de tinta a serem compradas e o preço
#total.



print('Bem vindo à cores belas tinturaria!\n')

area = int(input('Qual a medida em metros quadrados da área a ser pintada? '))

#é necessário dividir os metros quadrados em 3 para saber o
#numero de latas no entanto, precisamos arredondar esse
#numero para cima, porque não podemos permitir a compra
#de frações de latas de tinta

litros_de_tinta = area//3

#com os litros em mãos, o programa calcula o numero de
#latas de tinta, também em numeros inteiros

quantidade_de_latas = litros_de_tinta//18

#agora é só multiplicarmos pelo valor de cada lata de titna

preço_a_ser_pago = quantidade_de_latas*80

#e o restante é só informar os valores para o usuário

if quantidade_de_latas >= 1:
    print(f'Muito bem, o número total de latas necessário será {quantidade_de_latas} e o valor será de R${preço_a_ser_pago}')
else:
    print('Muito bem, o número total de latas necessário será 1 e o valor será de R$80,00')
