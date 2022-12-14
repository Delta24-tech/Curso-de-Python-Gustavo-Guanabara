frase = input("Digite uma frase: ")
dividido = frase.split()
i = 0
for i in range(len(dividido)):
    if dividido[i] == "A":
        print("A primeira letra A aparece na posição {}".format(i))
        break
for i in range(len(dividido)):
    if "A" in dividido:
        i+=1
print("Quantidade de letras A na frase: ",i)
