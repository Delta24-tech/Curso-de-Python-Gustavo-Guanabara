aluno = {}
x = list()
while True:
    aluno['nome'] = input("Digite o nome do aluno: ")
    aluno['média'] = float(input("Digite a média do aluno: "))
    x.append(aluno.copy())
    resp = input("Digite [S|s] para continuar ou [N|n] para parar: ")
    if resp in 'Nn':
        break
    

for e,v in aluno.items():
    print(f'O {e} é {v}')
    
    
