from math import sqrt, hypot
cateto_oposto = int(input("Digite o comprimento do cateto oposto: "))
cateto_adjascente = int(input("Digite o comprimento do cateto adjascente: "))
'''hipotenusa = cateto_oposto**2 + cateto_adjascente**2
print(hipotenusa)
hipotenusa = hypot(cateto_oposto, cateto_adjascente)
print(hipotenusa)'''
hipotenusa = (cateto_oposto**2 + cateto_adjascente**2) **(1/2)
print(hipotenusa)
