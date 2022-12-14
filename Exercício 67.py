while(True):
    i = 0
    n = int(input("Digite um número: "))
    for c in range(1,11):
        print
    if n < 0:
        break
    else:
        i+=1
        print("{}x{} = {}".format(n,i,n*i))
