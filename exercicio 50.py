soma = 0
for i in range(6):
   n1 = int(input(f'Digite o {i}°i número: '))
   if(n1%2==0):
       soma += n1
       cont += 1
print(f'A soma de todos os pares é de {soma}')
