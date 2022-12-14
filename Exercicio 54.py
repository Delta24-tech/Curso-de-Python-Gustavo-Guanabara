x = 0
y = 0
for i in range(7):
    n = int(input(f'Digite o ano de nascimento da {i}° pessoa'))
    if n >= 2005:
        x += 1
    else:
        y += 1
print(f'O número de pessoas que não alcançaram a maior idade é de: ',x)
print(f'O número de pessoas que alcançaram maior idade é de: ',y)


from datetime import date
atual = date.today().year
totmaior=0
totmenor=0
for pess in range(1,8):
  nasc = int(input("Em que ano a pessoa nasceu? "))
  idade = atual - nasc
  if idade >= 21:
    totmaior += 1
  else:
    totmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("E também tivemos {} pessoas menores de idade".format(totmenor))

