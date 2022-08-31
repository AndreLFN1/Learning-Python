
"""

for elemento in interável:
    faça algo

o uso do for (para)

tbm pode usar o else

Para cada 'elemento' dentro do 'interável':
    faça algo

"""
palavra = 'Python'

#não precisamos escrever letra, podemos colocar com qualquer sentido
for letra in palavra:
    print(letra)

#Resposta do console:
#P
#y
#t
#h
#o
#n

palavra = 'Laranja'

for posição, letra in enumerate(palavra):
    print(posição, letra)

#Resposta do console:
#0 L
#1 a
#2 r
#3 a
#4 n
#5 j
#6 a
