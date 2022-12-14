velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print("Você está acima do limite de velocidade. Será cobrada uma multa que custará" 
          "R$7,00 por cada Km acima do limite. O valor da multa será de {}".format(velocidade*7))
    
            
