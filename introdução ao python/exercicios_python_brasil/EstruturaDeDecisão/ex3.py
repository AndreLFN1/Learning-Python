'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

sexo = 'None'

while sexo != 'M':
    sexo = input('Qual o seu sexo? M/F ')
    if sexo == 'F':
        break


print(f' O sexo selecionado é: {sexo}')
