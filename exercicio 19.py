from random import randint, choice
lista = []
i = 0
while i <= 3:
    n1 = input("Digite o nome do {}° aluno".format(i+1))
    if n1 not in lista:
        lista.append(n1)
        i+=1
    else:
        print("Aluno repetido. Insira novamente")
        continue
print(lista)
'''1° solução'''
n1 = input("Digite o nome do 1° aluno: ")
n2 = input("Digite o nome do 2º aluno: ")
n3 = input("Digite o nome do 3° aluno: ")
n4 = input("Digite o nome do 4° aluno: ")
lista = [n1,n2,n3,n4]
print("O aluno escolhido pelo professor para apagar o quadro é o {}".format(choice(lista)))

'''2° solução'''
lista = [n1,n2,n3,n4]
valores = []
for aluno in lista:
    if aluno not in valores:
        valores.append(aluno)
    
for i in range(len(valores)):
    if(choice(valores) == valores[i]):
            print("O aluno escolhido pelo professor para apagar o quadro é o {}".format(valores[i]))
            break
'''3° solução'''
lista = []
valores = []
lista.append(n1)
lista.append(n2)
lista.append(n3)
lista.append(n4)
for aluno in lista:
  i = 0
  if aluno not in valores:
   valores.append(aluno)
   i+=1
  else:
     valores.pop(i)
     print("Alguns dos valores digitados estão repetidos. Tente novamente")
     s1 = input("Digite o nome do 1° aluno: ")
     s2 = input("Digite o nome do 2° aluno: ")
     s3 = input("Digite o nome do 3° aluno: ")
     s4 = input("Digite o nome do 4° aluno: ")
     if(i == 0):
       valores.insert(i,s1)
     if(i == 1):
       valores.insert(i,s2)
     if(i == 2):
       valores.insert(i,s3)
     if(i == 3):
       valores.insert(i,s4)
     lista.remove(n2)
     lista.remove(n3)
     lista.remove(n4)
     lista.append(s1)
     lista.append(s2)
     lista.append(s3)
     lista.append(s4)
     
     
print(lista)
print(valores)
print("O aluno escolhido pelo professor para apagar o quadro é o {}".format(choice(valores)))
            

