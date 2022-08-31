lista_de_compras = []
resposta = ' '

while resposta != 'Acabou':
    resposta = input('Qual item você deseja adcionar (se tiver terminado digite: Acabou): ')
    if resposta == 'acabou':
        break
    lista_de_compras.append(resposta)

print(lista_de_compras)
