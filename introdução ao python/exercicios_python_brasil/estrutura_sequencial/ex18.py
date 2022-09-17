'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
download do arquivo usando este link (em minutos).

'''

size = float(input('Qual o tamanho do arquivo? '))

internet_speed = float(input('Qual a velocidade da sua internet? (em Mbps) '))

tempo_download = size/(internet_speed/60)

print(f'O tempo de download será de {tempo_download} minutos!')
