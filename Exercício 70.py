total =0
totmil = 0
barato = ''
menor = 0
cont = 0
while True:
    produto = input("Digite o nome de um produto: ")
    preço = float(input("Digite o preço do produto: "))
    total+=preço
    cont+=1
    continuar = input("Deseja continuar cadastrando mais dados? [S|N]")
    if(preço>1000):
        totmil +=1
    if(cont == 1) or (preço < menor):
        menor = preço
        barato = produto
    if(continuar not in "SsNn"):
        continuar = input("Valor inválido. Digite [S|N]")
    if(continuar in "Nn"):
        break

print("O total gasto na compra é de {}".format(total))
print("O número de produtos que custam mais de 1000 é {}".format(totmil))
print("O nome do produto mais barato é {}".format(barato))

    
