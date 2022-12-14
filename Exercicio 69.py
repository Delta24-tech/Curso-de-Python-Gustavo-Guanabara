maior_idade = 0
quantidade_homens = 0
quantidade_mulheres_menos_20 = 0
while(True):
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa: [F|M]")
    if(idade >= 18):
        maior_idade+=1
    if(sexo in "Mm"):
        quantidade_homens+=1
    if(sexo in "Ff" and idade < 20):
        quantidade_mulheres_menos_20 += 1
        
        
    print("Os dados da pessoa foram cadastrados")
    continuar = input("Deseja continuar cadastrando mais pessoas?[S|N]")
    while continuar not in "SsNn":
        continuar = input("Deseja continuar cadastrando mais pessoas?[S|N]")
    if continuar in "Nn":
       break
    
print("A quantidade de mulheres cadastradas que possui menos de 20 anos é de {}".format(quantidade_mulheres_menos_20))
print("A quantidade homens cadastrados é de {}".format(quantidade_homens))
print("A quantidade de pessoas maiores de idade cadastradas é de {}".format(maior_idade))

