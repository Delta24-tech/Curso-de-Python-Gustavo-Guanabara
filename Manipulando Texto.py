frase = "Curso em Vídeo Python"
print(frase.upper().count("o"))
print(len(frase.strip())) #-> remove os espaços indesejados
frase = frase.replace("Python","Android")
dividido = frase.split()
print(dividido[0][1])
print(frase)
print("Curso" in frase)
print(frase.find("Curso"))
print(frase.lower().find("vídeo"))
print(frase[13:1])
print(frase[1:2])
print(frase[1::2])
print("OI")
print("""xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx""")
