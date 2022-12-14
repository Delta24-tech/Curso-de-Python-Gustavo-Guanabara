from random import randint
while(True):
    jogador = int(input("Digite um valor: "))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = input("Par ou Ímpar?").strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}',end=' ')
    print("DEU PAR" if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU")
        else:
            print("Você PERDEU")
    elif tipo == "I":
        if total % 2 == 0:
            print("Você VENCEU")
        else:
            print("Você PERDEU")
    print('Vamos jogar novamente...')
    
