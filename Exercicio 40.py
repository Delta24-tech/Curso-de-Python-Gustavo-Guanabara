nota1 = int(input("Digite uma nota: "))
nota2 = int(input("Digite outra nota: "))
media = (nota1+nota2)/2
print(media)
if(media < 5):
    print("REPROVADO!!!")
if(media >=5 and media <= 6.9):
    print("RECUPERAÇÃO")
if(media >=7):
    print("APROVADO")
