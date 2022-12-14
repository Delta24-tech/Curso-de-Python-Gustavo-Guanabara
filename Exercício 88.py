from random import randint
from time import sleep
jogos = []
número_jogos = int(input('Insira o número de jogos da MEGA SENA que serão gerados: '))
tot = 1
while tot <= número_jogos:
    lista = []
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('=' * 3, f' SORTEANDO {número_jogos} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(2)
print('-=' * 5, '<BOA SORTE! >', '-=' * 5)
