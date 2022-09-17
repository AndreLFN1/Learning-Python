'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma
ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo
grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

Se o delta calculado for negativo, a equação não possui raizes reais. Informe
ao usuário e encerre o programa;

Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

print('Bem vindo ao programa de cálculo de raizes de equações de segundo grau!')
#a formula é ax**2 + bx + c = 0
#obtemos o a:
a = float(input('Digite o valor de a: '))

#se a for zero, o programa deve ser encerrado
if a != 0:

    b = float(input('Digite o valor de b: '))

    c = float(input('Digite o valor de c: '))
    #calculo do delta
    delta = (b**2) - (4*a*c)

    #no caso de delta = 0, só há uma raíz real.
    if delta == 0:
        x = (-b)/(2*a)
        print(f'Como delta é zero, a equação tem apenas uma raíz real que é: {x}')

    elif delta > 0:
        #calculos da raiz de delta e das raízes da equação, atendido o if.
        raiz_de_delta = delta**(1/2)

        x_1 = (-b - raiz_de_delta)/(2*a)

        x_2 = (-b + raiz_de_delta)/(2*a)

        print(f'As raízes da equação são {x_1} e {x_2}.')

        #o else vai pegar o delta negativo, onde a equação não é valida.
    else:
        print('Como o delta é negativo, essa equação não tem raízes reais.')


else:

    print('Essa equação não é de segundo grau.')
