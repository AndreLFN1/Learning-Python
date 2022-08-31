idade = input('Qual sua data de nascimento? ')

lista_1 = idade.split('/')

#isso cria a seguinte lista: lista_1 = ['02', '04', '97'] dado que o usuário digitou
#02/04/97



print(f'{lista_1}')
print(f'Então você nasceu no dia {lista_1[0]} do mês {lista_1[1]} do ano de {lista_1[2]}!')
