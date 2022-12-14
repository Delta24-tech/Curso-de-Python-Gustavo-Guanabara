soma = 0
contador = 0
for i in range(1,501,2):
    if i%3 == 0: 
        soma += i
        contador += 1

print(f'A soma de todos os {contador} números ímpares e múltiplos de três é de {soma}')

#2°Solução
soma1 = 0
for i in range(1,501,2):
    if i%3 == 0:
        if i%2!=0:
            soma1 += i
    
print(f'A soma de todos os {contador} números ímpares e múltiplos de três é de {soma}')


#3°Solução
soma2 = 0
for i in range(1,501):
    if i%3 == 0:
        if i%2!=0:
            soma2+=i
print("A soma de todos os {contador} números ímpares e múltiplos de três é {soma2}")
