'''

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

altura = float(input('Qual a sua altura? '))
sexo = ' '

while sexo != 'm':
    sexo = input('Qual o seu sexo? (m/f) ')
    if sexo == 'f':
        break

if sexo == 'm':
    peso_ideal = (72.7*altura) - 58
else:
    peso_ideal = (62.1*altura) - 44.7

print(f'O seu peso ideal é {peso_ideal} quilogramas')
