boletim = []
while True:
    lista = []
    média = 0
    nome = input('Digite o nome do aluno: ')
    nota_1 = float(input('Digite a 1° nota do aluno: '))
    nota_2 = float(input('Digite a 2° nota do aluno: '))
    resp = input('Digite [S|s] para continuar ou [N|n] para parar: ')
    lista.append(nome)
    lista.append(nota_1)
    lista.append(nota_2)
    média=(nota_1+nota_2)/2
    lista.append(média)
    boletim.append([nome,[nota_1,nota_2],média])
    if(resp in 'Nn'):
        break
    else:
        continue
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i,a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
