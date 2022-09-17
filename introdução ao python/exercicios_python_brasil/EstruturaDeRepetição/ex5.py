'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas
de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
print('Descubra em quanto tempo a população de duas cidades vai ser igual, dado que a cidade menos populosa tenha uma taxa de crescimento maior do que a mais populosa!')

pop_A = int(input('Digite o numero de habitantes iniciais da cidade menos populosa: '))
taxa_A = float(input('Digite a taxa de crescimento da cidade menos populosa: '))


pop_B = int(input('Digite a quantidade de habitantes da cidade mais populosa: '))
taxa_B = float(input('Digite a taxa de crescimento populacional da cidade mais populosa: '))

anos = 0
while pop_A <= pop_B:
    anos += 1
    pop_A *= taxa_A
    pop_B *= taxa_B

pop_A = round(pop_A, 0)
pop_B = round(pop_B, 0)
print(f'Serão necessários {anos} anos para que a população A ultrapasse a população de B. ')
print(f'População da cidade A: {pop_A} habitantes')
print(f'População da cidade B: {pop_B} habitantes')
