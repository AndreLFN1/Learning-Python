texto = input('Escreva uma palavra ou frase: ')

vogal_a = texto.count('a')

vogal_e = texto.count('e')

vogal_i = texto.count('i')

vogal_o = texto.count('o')

vogal_u = texto.count('u')

espaços = texto.count(' ')


if vogal_a > 0 or vogal_e > 0 or vogal_i > 0 or vogal_o > 0 or vogal_u > 0:
    print('Seu texto tem vogais! E elas são: ')
if vogal_a > 0:
    print('a')
if vogal_e > 0:
    print('e')
if vogal_i > 0:
    print('i')
if vogal_o > 0:
    print('o')
if vogal_u > 0:
    print('u')
if espaços > 0:
    print('Além disso, o que você escreveu é uma frase!')

else:
    print('Seu texto não possui nenhuma vogal!')
