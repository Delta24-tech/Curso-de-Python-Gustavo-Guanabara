matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares = 0
soma_terceira_coluna = 0
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i},{j}]: '))

maior_segunda_linha = matriz[1][0]
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma_pares+=matriz[i][j]
        if matriz[1][j] > maior_segunda_linha:
            maior_segunda_linha = matriz[1][j]
    soma_terceira_coluna+=matriz[i][2]


for i in range(3):
    for j in range(3):
        print(f'{[matriz[i][j]]}',end='')
    print()
                

print(f'A soma de todos os valores pares é de: {soma_pares}')
print(f'A soma dos valores da terceira coluna é de: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')
        
