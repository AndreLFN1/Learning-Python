'''
Faça um Programa que leia 2 números e em seguida
pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

num_1 = float(input('Digite o primeiro numero! '))

num_2 = float(input('Digite o segundo numero! '))


operacao = input('Qual operação você deseja realizar? Digite: M (multiplicação), D (Divisão), A (Adição) e S (Subtração): ' )


if operacao == 'A':
    resultado = num_1 + num_2

elif operacao == 'S':
    resultado = num_1 - num_2

elif operacao == 'M':
    resultado = num_1*num_2

elif operacao == 'D':
    resultado = round(num_1/num_2, 2) #a fuição round determina quantas
    #casas apos a virgula terá a nossa divisão 

par_ou_ímpar = ''
negativo_ou_positivo = ''
inteiro_ou_decimal = ''

if resultado%2 == 0:
    par_ou_ímpar = 'Par!'
else:
    par_ou_ímpar = 'Ímpar!'

if resultado > 0:
    negativo_ou_positivo = 'Positivo!'
else:
    negativo_ou_positivo = 'Negativo!'

if (resultado - resultado//1) == 0:
    inteiro_ou_decimal = 'Inteiro!'
else:
    inteiro_ou_decimal = 'Decimal!'



print(f'''
Resultado: {resultado}
Seu numero é: {par_ou_ímpar}
Negativo ou positivo: {negativo_ou_positivo}
Inteiro ou decinal: {inteiro_ou_decimal}
''')
