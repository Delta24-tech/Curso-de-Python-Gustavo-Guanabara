#Simulador de Caixa Eletrônico
sacar = int(input("Digite o valor a ser sacado: "))
céd = 50
totcéd = 0
while True:
    if sacar >= céd:
        sacar -= céd
        totcéd += 1
    else:
        print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if sacar == 0:
            break
