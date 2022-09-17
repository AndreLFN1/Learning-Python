'''

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do
saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis
serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota
de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma
nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

'''


#o programa vai lidar com o operador % para determinar se o resto de uma operaçãop é zero

#precisamos executar uma série de decisões if em sequencia para sabermos o resultado

#podemos primeira pensar em casoas mais simples:



#aqui vamos reeber o valor que o usuário deseja retirar do caixa

saque = int(input('Quanto você deseja sacar em dinheiro? (entre R$10,00 e R$600,00) '))


while saque < 10 or saque > 600:
    saque = int(input('O valor tem que estar entre R$10,00 e R$600,00. Informe um novo valor.'))


#primeiro o programa pegar o valor de saque e divide por 100 obtendo o valor inteiro:


numero_notas_100 = int(saque/100) # --> 2
#print(numero_notas_100) # 2


resto_saque = saque - numero_notas_100*100 # 278 - 200 = 78

numero_notas_50 = int(resto_saque/50) # 78/50 = 1
#print(numero_notas_50)

resto_saque = resto_saque - numero_notas_50*50 # 78 - 50 = 28

numero_notas_10 = int(resto_saque/10) # 28/10 = 2
#print(numero_notas_10)

resto_saque = resto_saque - numero_notas_10*10 # 28 - 2*10 = 8

numero_notas_5 = resto_saque//5 #8//5 = 1
#print(numero_notas_5)

resto_saque = resto_saque - numero_notas_5*5 #8 - 1 = 3

numero_notas_1 = resto_saque
#print(numero_notas_1)

print(f'''
SAQUE
Notas de R$100,00: {numero_notas_100}
Notas de R$50,00: {numero_notas_50}
Notas de R$10,00: {numero_notas_10}
Notas de R$5,00: {numero_notas_5}
Notas de R$1,00: {numero_notas_1}
'''

)
