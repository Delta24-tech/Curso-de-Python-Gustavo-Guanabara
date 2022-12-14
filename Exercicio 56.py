media = 0
lista_nome = []
lista_idade = []
lista_sexo = []
nomevelho = ''
maioridadehomem = 0
totmulher20 = 0
somaidade = 0
for p in range(1,5):
    nome = input(f'Digite o nome da {p}° pessoa').strip()
    idade = int(input(f'Digite a idade da {p}° pessoa'))
    sexo = input(f'Digite o sexo da {p}° pessoa [M/F]')
    lista_nome.append(nome)
    lista_idade.append(idade)
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20+=1

media = somaidade/4


print(f'A média de idade do grupo é de {media} anos')
print(f'O nome do homem mais velho é {nomevelho}')
print(f'O número de mulher que têm menos de 20 anos é {totmulher20}')
    
    
