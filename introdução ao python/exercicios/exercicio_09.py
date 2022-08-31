'''
Ex. 09
Faça um programa que paça uma nota entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um
valor válido.

'''

nota = float(input('Dê uma nota de zero a dez!  '))

while nota < 0 or nota > 10:
    nota = float(input('Não, é sério, digite uma nota aí! '))

print(f'A nota que você deu foi {nota}')
