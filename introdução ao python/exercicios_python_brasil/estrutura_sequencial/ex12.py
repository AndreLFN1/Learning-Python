'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''

altura_fornecida = float(input('Qual a sua altura? '))

peso_ideal = (72.7*altura_fornecida) - 58

print(f'O seu peso ideal é de {peso_ideal} quilogramas')
