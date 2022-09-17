'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne
da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for
feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um
cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.

'''
#inputs

tipo_carne = int(input('Qual será a carne comprada? Digite 1 para File Duplo; 2 para Alcatra e 3 para Picanha: '))

peso_da_carne = float(input('Qual o peso em Kg de carne você deseja? '))

forma_de_pagamento = int(input('O pagamento será no cartão da loja? Digite 1 para sim e 2 para dinheiro: '))

#corpo do programa

if peso_da_carne <= 5:

    if forma_de_pagamento == 1:

        if tipo_carne == 1:
            valor_da_compra = peso_da_carne*4.90
            desconto = round(valor_da_compra*0.05, 2)
            valor_a_ser_pago = valor_da_compra - desconto

        elif tipo_carne == 2:
            valor_da_compra = peso_da_carne*5.90
            desconto = round(valor_da_compra*0.05, 2)
            valor_a_ser_pago = valor_da_compra - desconto

        elif tipo_carne == 3:
            valor_da_compra = peso_da_carne*6.90
            desconto = round(valor_da_compra*0.05, 2)
            valor_a_ser_pago = valor_da_compra - desconto

    else:
        if tipo_carne == 1:
            valor_a_ser_pago = peso_da_carne*4.90

        elif tipo_carne == 2:
            valor_a_ser_pago = peso_da_carne*5.90

        elif tipo_carne == 3:
            valor_a_ser_pago = peso_da_carne*6.90

else:

    if forma_de_pagamento == 1:

        if tipo_carne == 1:
            valor_da_compra = peso_da_carne*5.80
            desconto = round(valor_da_compra*0.05, 2)
            valor_a_ser_pago = valor_da_compra - desconto

        elif tipo_carne == 2:
            valor_da_compra = peso_da_carne*6.80
            desconto = round(valor_da_compra*0.05, 2)
            valor_a_ser_pago = valor_da_compra - desconto

        elif tipo_carne == 3:
            valor_da_compra = peso_da_carne*7.80
            desconto = round(valor_da_compra*0.05, 2)
            valor_a_ser_pago = valor_da_compra - desconto

    else:
        if tipo_carne == 1:
            valor_a_ser_pago = peso_da_carne*5.80

        elif tipo_carne == 2:
            valor_a_ser_pago = peso_da_carne*6.80

        elif tipo_carne == 3:
            valor_a_ser_pago = peso_da_carne*7.80



if tipo_carne == 1:
    tipo_carne = 'Filé Duplo'
elif tipo_carne == 2:
    tipo_carne = 'Alcatra'
elif tipo_carne == 3:
    tipo_carne = 'Picanha'

if forma_de_pagamento == 1:
    forma_de_pagamento = 'Cartão da Loja'
elif forma_de_pagamento == 2:
    forma_de_pagamento = 'Dinheiro'

#output
print(f'''
CUPOM FISCAL
Tipo de pagamento: {forma_de_pagamento}; R${desconto} de desconto
Produto: {tipo_carne} - {peso_da_carne}Kg
Preço total (com desconto): R${valor_a_ser_pago}
''')
