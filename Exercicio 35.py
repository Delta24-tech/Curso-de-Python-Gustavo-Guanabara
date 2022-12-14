valor_da_casa = float(input("Digite o valor da casa: "))
salario_do_comprador = float(input("Digite o salário do comprador: "))
anos = int(input("Digite a quantidade de anos em que ele vai pagar a casa: "))
prestação = casa/(anos*12)
mínimo = salário * 30/100
print("Para pagar uma casa de R${:.2f} em {} anos".format(casa,anos),end='')
print("a prestação será de R${:.2f}".format(prestação))
print("COMPARANDO tem que pagar {} e o mínimo é de {}".format(prestação,mínimo))
if prestação <= mínimo:
    print("Empréstimo pode ser CONCEDIDO")
else:
    print("Empréstimo NEGADO!")
    
