nome = input("Digite seu nome completo: ")
dividido = nome.split()
for i in range(len(dividido)):
    if "Silva" in nome:
        if dividido[i] == "Silva":
            print('{} tem Silva em seu nome e a palavra Silva aparece na posição {}'.format(nome,i))
    else:
     print('{} não tem Silva em seu nome'.format(nome))
