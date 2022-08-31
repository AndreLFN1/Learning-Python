'''
Ex. 11

Faça um programa que itera em uma string e toda vez que uma vogal aparecer
na sua string print o seu nome entre as letras

string = bananas

b
Andre
a
Andre
.
.
.

'''
vogais = 'aeiou'
palavra = 'babanas'
nome = 'Andre'
for x in palavra:
    if x == 'a' or x == 'i' or x == 'o' or x == 'u':
        print(nome)
    else:
        print(x)

print('*'*100)

for letra in palavra:
    if letra in vogais:
        print(nome)
    else:
        print(letra)
