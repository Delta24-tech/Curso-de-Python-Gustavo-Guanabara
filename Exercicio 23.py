while(True):
    numero = input("Digite um numero entre 0 até 9999: ").split(" ")
    if(int(numero[0]) < 0 or int(numero[0]) > 9999) and (int(numero[1]) < 0 or int(numero[1] > 9999)):
        print("O número digitado é inválido")
        continue
    break
    
dividido = numero.split()
for i in range(len(dividido)):
    if int(dividido[i]) >=0 and int(dividido[i]) <= 9:
     print("unidade:",dividido[0][1])
    
    if int(dividido[i]) >= 10 and int(dividido[i]) <= 99:
     print("unidade:",dividido[0][1])
     print("dezena:",dividido[0][0])
    
    if int(dividido[i]) >= 100 and int(dividido[i]) <= 999:
     print("unidade:",dividido[0][2])
     print("dezena:",dividido[0][1])
     print("centena:",dividido[0][0])
    if int(dividido[i]) >= 1000 and int(dividido[i]) <= 9999:
     print("unidade:",dividido[0][3])
     print("dezena:",dividido[0][2])
     print("centena:",dividido[0][1])
     print("milhar:",dividido[0][0])

for i in dividido:
    if int(i) >= 0 and int(i) <= 9:
        print("unidade:",dividido[i][1])
    
        
