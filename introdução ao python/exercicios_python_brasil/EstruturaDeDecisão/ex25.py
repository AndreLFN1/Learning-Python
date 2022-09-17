'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".

'''
telefonou = input('Você telefonou para a vítima? ')

esteve_no_local = input('Você esteve no local do crime? ')

mora_perto = input('Você mora perto da vítima? ')

devia_para_vitima = input('Você tinha uma dívida para com a vítima? ')

ja_trabalhou_com_a_vitima = input('Você já trabalhou com a vítima? ')

contagem_suspeicao = 0

if telefonou == 'sim':
    contagem_suspeicao += 1
else:
    contagem_suspeicao == contagem_suspeicao
if esteve_no_local == 'sim':
    contagem_suspeicao += 1
else:
    contagem_suspeicao == contagem_suspeicao
if mora_perto == 'sim':
    contagem_suspeicao += 1
else:
    contagem_suspeicao == contagem_suspeicao
if devia_para_vitima == 'sim':
    contagem_suspeicao += 1
else:
    contagem_suspeicao == contagem_suspeicao
if ja_trabalhou_com_a_vitima == 'sim':
    contagem_suspeicao += 1
else:
    contagem_suspeicao == contagem_suspeicao

if contagem_suspeicao == 2:
    veredito = 'Suspeite!'
elif 3 <= contagem_suspeicao <= 4:
    veredito = 'Cúmplice!'
elif contagem_suspeicao == 5:
    veredito = 'Culpade!'
else:
    veredito == 'Inocente!'

print(f'''
Veredicto:
Você respondeu afirmativamente à {contagem_suspeicao} perguntas.
Devido à isso você é considerade {veredito}!
''')
