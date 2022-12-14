def ficha(nome_jogador,número_gols):
    print('------------Ficha do Jogador-----------')
    print(f'O nome do jogador é {nome_jogador}')
    print(f'O número de gols marcado por {nome_jogador} é de {número_gols}')
    
n = input('Nome do Jogador: ')
g = input('Número de Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == ' ':
    ficha(número_gols=g)
else:
    ficha(n,g)
