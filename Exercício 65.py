n = [int(n) for n in input("Entre com múltiplos valores:").split(" ")]
soma = 0
media = 0
maior = n[len(n)-1]
menor = n[0]
for x in n:
    soma+=x
    if(x > maior):
        maior = x
    if(x < menor):
        menor = x

print("O maior valor do array é {}".format(maior))
print("O menor valor do array é {}".format(menor))
print("A média dos valores é de {}".format(soma/len(n)))
  

resp = "S"
quant = media = maior_1 = menor_1 = 0
while resp in "Ss":
    núm = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior_1 = menor_1 = núm
    else:
        if núm > maior_1:
            maior_1 = núm
        if núm < menor_1:
            menor_1 = núm
    resp = input("Quer continuar[S/N]").upper().strip()[0]
media = soma/quant
print("Você digitou {} números e a média foi {}".format(quant,média))
print("O maior valor foi {} e o menor foi {]".format(maior,menor))
    
