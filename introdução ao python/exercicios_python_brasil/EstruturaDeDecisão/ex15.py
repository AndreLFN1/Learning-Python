'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

#inputs do  usuario sobre o tamanho dos lados dos triângulos
lado_1 = float(input('Digite o tamanho do primeiro lado do triângulo: '))

lado_2 = float(input('Digite o tamanho do segundo lado do triângulo: '))

lado_3 = float(input('Digite o tamanho do terceiro lado do triângulo: '))

#somas possíveis
soma_1 = lado_1 + lado_2
soma_2 = lado_1 + lado_3
soma_3 = lado_2 + lado_3


#condicionais. A variável tipo_triangulo vai servir para definir o tipo
#de triangulo nos condicionais

tipo_triangulo = ' '

if soma_1 > lado_3 or soma_2 > lado_2 or soma_3 > lado_1:
    if lado_1 == lado_2 and lado_1 == lado_3:
        tipo_triangulo = 'Equilátero'
    elif lado_1 == lado_2 or lado_1 == lado_3:
        tipo_triangulo = 'Isósceles'
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        tipo_triangulo = 'Escaleno'

    print(f'''Esse valores formam um triângulo válido!

        E este é um triângulo {tipo_triangulo}!
    ''')

else:
    print('Esse não é um triângulo válido!')
