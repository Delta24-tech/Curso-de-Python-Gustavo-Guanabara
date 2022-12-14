from time import sleep
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
opção = 0
while(opção!=5):
    print('''
    [1] somar
    [2] subtrair
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
     soma = n1 + n2
     print('A soma entre {} + {} é {}'.format(n1,n2,soma))
    elif opção == 2:
     subtração = n1 - n2
     print("A subtração entre {} - {} é {}".format(n1,n2,subtração))
    elif opção == 3:
     if n1 > n2:
        print(f'{n1} é maior que {n2}')
     elif n2 > n1:
        print(f'{n2} é maior que {n1}')
     else:
        print("Os números são iguais")
    elif opção == 4:
      print("Informe os números novamente")
      n1 = int(input("Primeiro valor: "))
      n2 = int(input("Segundo valor: "))
    elif opção ==5:
     print("Finalizando")
    else:
        print("Opção inválida. Tente novamente")
    print("=-="*10)
print("Fim do programa! Volte sempre!")

