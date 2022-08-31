nota_1 = float(input('Olá, qual foi a sua primeira nota? '))
nota_2 = float(input('Olá, qual foi a sua segunda nota? '))

media = (nota_1 + nota_2)/2

if media >= 7 and media < 10:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
elif media == 10:
    print('Aprovado com distinção!')
