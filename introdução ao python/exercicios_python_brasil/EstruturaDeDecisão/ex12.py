'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
 dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a
 quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

'''
#inputs de valor e horas trabalhadas
valor_hora = float(input('Quanto o funcionário ganha por hora? '))

horas_trabalhadas = int(input('Por quantas horas o funcionário trabalha por mês? '))
#calculo do Bruto
bruto = valor_hora*horas_trabalhadas

#calculo de IR

if bruto <= 900:
    ir = 0
    desconto_ir = '0%'
elif 900 < bruto <= 1500:
    ir = bruto*0.05
    desconto_ir = '5%'
elif 1500 < bruto <= 2500:
    ir = bruto*0.10
    desconto_ir = '10%'
elif bruto >= 2500:
    ir = bruto*0.20
    desconto_ir = '20%'

#calculo do inss, fgts e descontos

inss = bruto*0.10

fgts = bruto*0.11

total_descontos = ir + inss

#salario Liquido

liquido = bruto - total_descontos


print(f'''
           Folha de pagamento

Salário Bruto                   : R$ {bruto}
(-) IR ({desconto_ir})                    : R$ {ir}
(-) INSS ( 10%)                 : R$ {inss}
FGTS (11%)                      : R$ {fgts}
Total de descontos              : R$ {total_descontos}
Salário Liquido                 : R$ {liquido}

''')
