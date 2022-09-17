'''

Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''
import calendar
import datetime

ganho_hora = float(input('Quanto você ganha por hora? '))

horas_trabalhadas_mes = int(input('Quantas horas você trabalha por mês?'))


print(f'O seu salário neste mês é: {horas_trabalhadas_mes*ganho_hora}')
