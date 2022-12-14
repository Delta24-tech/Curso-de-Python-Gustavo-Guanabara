from math import sin,cos,  radians 
angulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
print("O ângulo de {} tem o seno de {:.2f}".format(angulo,seno))
cosseno = cos(radians(angulo))
print("O ângulo de {} tem o cosseno de {:.2f}".format(angulo,cosseno))
tangente = tan(radians(ângulo))
print("O ângulo de {} tem a tangente de {:.2f}".format(angulo,tangente))

