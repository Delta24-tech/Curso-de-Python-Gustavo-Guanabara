from random import randint
x = 0
computador = randint(0,10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será qur você consegue adivinhar qual foi?")
while(True):
 numero = int(input("Dê um palpite. Digite um número entre 0 e 10: "))
 if(numero == computador):
    print("O número que o usuário digitou e o número sorteado batem. O número é {}".format(computador))
    x+=1
    break
 else:
    print("Os números não batem. O número que o usuário digitou é {} e o número sorteado é {}".format(numero,computador))
    x+=1
    continue
print(f'A quantidade necessária de vezes para acertar o número foi de {x}')
