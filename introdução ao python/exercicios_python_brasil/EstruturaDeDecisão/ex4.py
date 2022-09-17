'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

vogais = ['a', 'e', 'i', 'o', 'u']

letra = input('Digite uma letra: ')
i = 1
y = 0

while i <= len(vogais):
    if letra == vogais[i-1]:
        print('Há uma vogal aqui!!')
        y += 1
        i += 1
    else:
        i += 1

if y == 0:
    print('Isso não é uma vogal!')
