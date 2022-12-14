lista= []
i = 0
numero = input("Digite um número: ").split(" ")
for i, v in enumerate(numero):
    if(int(v) < 0 or int(v) > 9999) or v in numero[i+1:]:
      #print("O número que você digitou é inválido! Digite um número maior do que 0 ou menor do 9999")
      numero.remove(v)
      while True:
          novo_numero = input(f"Número inválido! O número digitado é maior do que 9999, menor do que 0 ou está repetido. Digite um número para substituir o número {v}: ")
          if(int(novo_numero) > 0 and int(novo_numero) < 9999) and novo_numero not in numero:
              print(f'O número {v} foi substituído por {novo_numero} na posição {i} do vetor')
              numero.insert(i, novo_numero)
              break

        
          
   
   
list[::-1]        
        

print(numero)   
for j in range(len(numero)):
  if int(numero[j]) >=0 and int(numero[j]) <= 9:
       print("{}° elemento da lista\n".format(j+1)) 
       print("unidade:",numero[j][0])
       print("\n")
    
  elif int(numero[j]) >= 10 and int(numero[j]) <= 99:
       print("{}° elemento da lista\n".format(j+1))
       print("unidade:",numero[j][1])
       print("dezena:",numero[j][0])
       print("\n")
    
  elif int(numero[j]) >= 100 and int(numero[j]) <= 999:
       print("{}° elemento da lista\n".format(j+1))
       print("unidade:",numero[j][2])
       print("dezena:",numero[j][1])
       print("centena:",numero[j][0])
       print("\n")
  elif int(numero[j]) >= 1000 and int(numero[j]) <= 9999:
       print("{}° elemento da lista\n".format(j+1))
       print("unidade:",numero[j][3])
       print("dezena:",numero[j][2])
       print("centena:",numero[j][1])
       print("milhar:",numero[j][0])
       print("\n")
 
