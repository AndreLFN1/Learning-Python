'''

As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

'''

salario_antes = float(input('Qual o seu salário atual? '))

if salario_antes <= 280:
    percentual = '20%'
    valor_aumento = salario_antes*0.20
    salario_novo = salario_antes*1.20

elif 280 < salario_antes <= 700:
    percentual = '15%'
    valor_aumento = salario_antes*0.15
    salario_novo = salario_antes*1.15
elif 700 < salario_antes <= 1500:
    percentual = '10%'
    valor_aumento = salario_antes*0.10
    salario_novo = salario_antes*1.10
elif 1500 < salario_antes:
    percentual = '5%'
    valor_aumento = salario_antes*0.05
    salario_novo = salario_antes*1.05




print(f'''

Salário antes do reajuste: R${salario_antes}

Percentual de aumento aplicado: R${percentual}

Valor do aumento: R${valor_aumento}

Novo salário: R${salario_novo}

''')
