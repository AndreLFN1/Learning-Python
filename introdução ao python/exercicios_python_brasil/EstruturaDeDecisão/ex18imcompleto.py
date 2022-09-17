'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se
a mesma é uma data válida.

1 Cada uma das 12 divisões do ano solar, sendo quatro (abril, junho, setembro e novembro)
com 30 dias, sete (janeiro, março, maio, julho, agosto, outubro e dezembro) com 31 dias e o
único mês, fevereiro, com 28 dias (ou 29 dias, nos anos bissextos): “O indicador de unha
suja de tinta de máquina de escrever percorre os trinta dias do mês de junho no
Almanaque do Pensamento” (CFA).
'''

#pegando a data
data = input('Digite uma data no formatyo dd/mm/aaaa: ')


#criando uma lista de comprimento 3 com dia, mes e ano
lista_data_str = data.split('/')

#essa lista vazia conterá apenas os valores convertidos em numeros inteiros
lista_data_int = []

#aqui vamos adcionar os numeros da data em uma lista e transformá-los em numeros
#pois anteriormente são registrados como strings
i = 0
while i < 3:
    lista_data_int.append(int(lista_data_str[i]))
    i += 1



#condicional para determinar se o mês de fevereiro terá 28 ou 29 dias naquele ano
fev_29_dias = 'não'

#condicional para determinar na frente se o mes terá 30 dias ou não
mes_30_dias = 'não'

#condicional para determinar na frente se o mes terá 31 dias ou não
mes_31_dias = 'não'




#condicional de ano bissexto. Caso seja, o mês de fevereiro desse ano deve
#ter 29 dias, caso não, terá 28 dias
if lista_data_int[2]%4 == 0:
    fev_29_dias = 'sim'


#definição de se o mês é de 31 dias
elif lista_data_int[1] == 4 or lista_data_int[1] == 6 or lista_data_int[1] == 9 or lista_data_int[1] == 11:
    mes_30_dias = 'sim'


#verificação de se o ano é bissexto ou não para determinar se fevereiro tem 28 ou 29 dias
elif lista_data_int[1] == 1 or lista_data_int[1] == 3 or lista_data_int[1] == 5:
    mes_31_dias = 'sim'

elif lista_data_int[1] == 7 or lista_data_int[1] == 8 or lista_data_int[1] == 10 or lista_data_int[1] == 12:
    mes_31_dias = 'sim'


#variáveis de validade. No final as três precisam ser atendidas para que o ano seja validado
dia = 'inválido'
ano = 'inválido'
mes = 'inválido'


#aqui vamos fazer todas as validações necessárias para confirmar se a data fornecida é válida
#primeiro verificamos se o ano é válido
if lista_data_int[2] >= 1:
    ano = 'válido'


#validação do mês
if 1 <= lista_data_int[1] <= 12:
    mes = 'válido'

#avaliando o mes de fevereiro se o ano for bissexto
if fev_29_dias == 'sim':
    #avaliando se o dia de fato tem até 29 dias
    if 1 <= lista_data_int[0] <= 29:
        mes = 'válido'

#avaliando o mes de fevereiro se o ano não for bissexto
if fev_29_dias == 'não':
    #avaliando se o dia de fato tem até 30 dias
    if 1 <= lista_data_int[0] <= 28:
        mes = 'válido'


#avaliando se o mes tem 30 dias e logo em seguida verificando se o dia é válido
if mes_30_dias == 'sim':
    #avaliando se o dia de fato tem até 30 dias
    if 1 <= lista_data_int[0] <= 30:
        mes = 'válido'


#avaliando se o mes tem 31 dias e logo em seguida verificando se o dia é correto
if mes_31_dias == 'sim':
    #avaliando se o dia de fato tem até 30 dias
    if 1<= lista_data_int[1] <= 31:
        mes = 'válido'


#finalizando o programa e informando o usuário se a data é válida
#uma série de validações é feita para avisar o usuário o que está incorreto
if dia == 'válido' and mes == 'válido' and ano == 'válido':
    print('A data é válida!')

elif dia != 'válido' and mes == 'válido' and ano == 'válido':
    print('A data é incorreta. O dia não é válido!')

elif dia == 'válido' and mes != 'válido' and ano == 'válido':
    print('A data é incorreta. O mês não é válido!')

elif dia == 'válido' and mes == 'válido' and ano != 'válido':
    print('A data é incorreta. O ano não é válido!')

elif dia != 'válido' and mes != 'válido' and ano == 'válido':
    print('A data é incorreta. O dia e o mês não são válidos!')

elif dia != 'válido' and mes == 'válido' and ano != 'válido':
    print('A data é incorreta. O dia e o ano não são válidos!')



else:
    print('Essa data não é correta!')











###
