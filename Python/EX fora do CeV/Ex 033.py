r1 = float(input("Digite o primeiro lado: ")) 
r2 = float(input("Digite o segundo lado: ")) 
r3 = float(input("Digite o terceiro lado: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 and r1 == r3:
        forma = "equilátero"
    elif r1 != r2 and r2 != r3 and r3 != r1:
        forma = "escaleno"
    else:
        forma = "isóceles"
    print(f"Pode formar um triângulo {forma}")
else:
    print("Não pode formar um triângulo")