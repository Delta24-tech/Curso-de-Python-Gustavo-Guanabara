matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    matriz[i] = [0]*3
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para preencher a posição {[i]}{[j]}: '))

for i in range(3):
    for j in range(3):
        print(f'{[matriz[i][j]]}',end='')
    print()

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]',end='')
    print()
    

    
