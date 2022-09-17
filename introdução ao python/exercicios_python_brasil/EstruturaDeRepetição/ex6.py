'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.
'''
i = 1
for x in range(20):
    print(i)
    i += 1

for x in range(1,21):
    print(x, end=' ') #esse end determina como o codigo deve parar. A finalização
    #de um print no python é por padrã /n, aqui deixamos o espaço
