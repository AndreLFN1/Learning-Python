'''

Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.

'''

num = int(input('Digite um numero para virar um dia da semana: '))

while num < 1 or num > 7:
    num = int(input('Valor inválido. Digite um numero entre 1 e 7: '))


if num == 1:
    print('Domingo')

elif num == 2:
    print('Segunda-feira')

elif num == 3:
    print('Terça-feira')

elif num == 4:
    print('Quarta-feira')

elif num == 5:
    print('Quinta-feira')

elif num == 6:
    print('Sexta')

elif num == 7:
    print('Sábado')
