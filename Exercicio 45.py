from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual é a sua jogada: \n"))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print("-="*11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-="*11)
if computador == 0:
    if jogador == 0:
        print("Jogo empatado")
    elif jogador == 1:
        print("O jogador ganhou.")
    elif jogador == 2:
        print("O computador ganhou.")
    else:
        print("JOGADA INVÁLIDA")
if computador == 1:
    if jogador == 0:
        print("O computador ganhou")
    elif jogador == 1:
        print("Jogo empatado")
    elif jogador == 2:
        print("O jogador ganhou")
    else:
        print("JOGADA INVÁLIDA")
if computador == 2:
    if jogador == 0:
        print("O jogador ganhou")
    elif jogador == 1:
        print("O jogador ganhou")
    elif jogador == 2:
        print("Jogo empatado")
    else:
        print("JOGADA INVÁLIDA")

        
    
