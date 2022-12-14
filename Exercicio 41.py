from datetime import date
atual = date.today().year
nascimento = int(input("Digite o ano de nascimento do atleta"))
idade = atual - nascimento
print("O atleta tem {} anos".format(idade))
if idade <= 9:
    print("Classificaçao: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 20:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")
