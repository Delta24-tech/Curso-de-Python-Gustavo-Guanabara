lista = []
for i in range(5):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    lista.append(peso)
maior = lista[0]
menor = lista[0]
for i in range(5):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]

print(f'O maior peso lido foi {maior}')
print(f'O menor peso lifo foi {menor}')

for p in range(1,6):
    peso = float(input("Peso da {}ª pessoa: ".format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}kg".format(maior))
print("O menor peso lido foi de {}kg".format(menor))
