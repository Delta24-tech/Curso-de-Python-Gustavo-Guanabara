from random import randint
numero = int(input("Digite um número entre 0 e 5: "))
num = randint(0,5)
if(numero == num):
    print("O número que o usuário digitou e o número sorteado batem. O número é {}".format(num))
else:
    print("Os números não batem. O número que o usuário digitou é {} e o número sorteado é {}".format(numero,num))
