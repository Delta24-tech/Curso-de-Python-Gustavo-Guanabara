primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
décimo = primeiro + (10-1)*razao
mais = 10
i = 2
while(i <= 10):
    print("O {} termo da PA é {}".format(i,primeiro +(i-1)*razao))
    i+=1
 
