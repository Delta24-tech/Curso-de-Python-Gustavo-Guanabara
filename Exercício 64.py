c = 0
soma = 0
while(True):
    n = int(input("Digite um número: "))
    soma+=n
    c+=1
    if n == 999:
        break
print("A quantidade de valores digitados é de {}".format(c))
print("A soma entre os números foi de {}".format(soma))


núm = cont = soma =  0
while(núm!=999):
 núm = int(input("Digite um número [999 para parar]: "))
 soma += núm
 cont += 1
print("Você digitou {} números e a soma entre eles foi {}".format(cont,soma))


