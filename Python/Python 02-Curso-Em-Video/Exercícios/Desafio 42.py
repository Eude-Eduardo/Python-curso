r1 = float(input("Digite o 1º segmento:"))
r2 = float(input("Digite o 2º segmento:"))
r3 = float(input("Digite o 3º segmento:"))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 >r1:
    print("pode formar um triângulo")
    if r1 == r2 and r1 == r3:
        print(f"E é um triângulo Equilátero")
    elif r1 == r2 or r1 == r3 or r2 == r3 :
        print(f"E é um triângulo Isóceles")
    else:
        print(f"E é um triângulo Escaleno")
else:
    print("Não pode formar um triângulo")

