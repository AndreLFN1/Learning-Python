'''
Faça um programa que leia um nome de usuário e a sua senha e não
aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e
voltando a pedir as informações.
'''

nome_de_usuario = input('Digite um nome de usuário: ')

senha = input('Digite uma senha: ')

if nome_de_usuario == senha:
    while nome_de_usuario == senha:
        senha = input('Senha igual ao nome de usuário. Digite outra senha: ')


print(f'O nome de usuário é {nome_de_usuario} e a senha é {senha}.')
