'''
Faça um programa que leia 5 números e informe o maior números

'''

i = 1

numero_guardado = float(input(f'Digite o numero {1}: '))

while i < 5:
    numero_novo = float(input(f'Digite o numero  {i+1}: ' ))
    i += 1

    if numero_novo > numero_guardado:
        numero_guardado = numero_novo

print(f'O maior numero digitado foi: {numero_guardado}')
