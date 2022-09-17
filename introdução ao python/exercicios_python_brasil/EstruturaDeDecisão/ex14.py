'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito
for A, B ou C ou “REPROVADO” se o conceito for D ou E.

'''
primeira_nota = float(input('Digite a sua primeira nota: '))

segunda_nota = float(input('Digite a sua segunda nota: '))

media = (primeira_nota + segunda_nota)/2

if 9 <= media <= 10:
    conceito = 'A'
    desfecho = 'APROVADO'
elif 7.5 <= media < 9:
    conceito = 'B'
    desfecho = 'APROVADO'
elif 6 <= media < 7.5:
    conceito = 'C'
    desfecho = 'APROVADO'
elif 4 <= media < 6:
    conceito = 'D'
    desfecho = 'REPROVADO'
elif 0 <= media < 4:
    conceito = 'E'
    desfecho = 'REPROVADO'

print(f'''
        BOLETIM

Nota 1: {primeira_nota}
Nota 2: {segunda_nota}
Média: {media}
Conceito final: {conceito}
Desfecho: {desfecho}
''')
