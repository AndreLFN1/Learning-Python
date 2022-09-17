'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
nome = input('Qual o seu nome? ')

while len(nome) <= 3:
    nome = input('Nome inválido. Digite um nome com mais de três caracteres: ')


idade = int(input('Digite sua idade: '))

while idade < 0 or idade > 150:
    idade = int(input('Idade inválida. Digite uma idade válida: '))

salario = float(input('Qual o seu salário atual? '))

while salario <= 0:
    salario = float(input('Salário inválido. Digite um valor maior que zero: '))

sexo = input('Qual o seu sexo? (f: feminimo; m: masculino) ')


while not (sexo == 'f' or sexo =='m'): #esse foi o modo que encontrei de contornar o problema dos or's no while, mas nao entendi pq funcionou
    sexo = input('Sexo inválido. Digite um sexo válido: ')

estado_civil = input('Qual o seu estado civil? (s: solteiro; c: casado; v: viuve; d: divorciado: )')

while not (estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd' ):
    estado_civil = input('Estado civil inválido. Digite um estado civil válido: ')


print(f'''
FICHA:
Nome: {nome}
Idade: {idade}
Salário: R${salario}
Sexo: {sexo}
Estado Civil: {estado_civil}
''')
