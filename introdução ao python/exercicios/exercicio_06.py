preço_1 = float(input('Qual o preço do primeiro produto? '))
preço_2 = float(input('Qual o preço do segundo produto? '))
preço_3 = float(input('Qual o preço do terceiro produto? '))


if preço_1 < preço_2 and preço_1 <  preço_3:
    print('Compre o primeiro produto')

elif preço_2 < preço_1 and preço_2 <  preço_3:
    print('Compre o segundo produto')

elif preço_3 < preço_1 and preço_3 <  preço_2:
    print('Compre o terceiro produto')
