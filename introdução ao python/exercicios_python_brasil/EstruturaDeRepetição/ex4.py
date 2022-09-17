'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa
de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
taxas de crescimento.
'''

pop_A = 80000

pop_B = 200000

anos = 0
while pop_A <= pop_B:
    anos += 1
    pop_A *= 1.03
    pop_B *= 1.015

pop_A = round(pop_A, 0)
pop_B = round(pop_B, 0)
print(f'Serão necessários {anos} anos para que a população A ultrapasse a população de B. ')
print(f'População da cidade A: {pop_A} habitantes')
print(f'População da cidade B: {pop_B} habitantes')
