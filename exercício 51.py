primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
décimo = primeiro + (10-1)*razao
for i in range(primeiro,10,razao):
    print('{}'.format(i),end=' -> ')
print("ACABOU")
 
