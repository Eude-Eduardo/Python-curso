n1 = int(input("Digite  um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais umnúmero: "))

if n1 > n2:
    print("O primeiro número é maior")
elif n2 > n1 and n2 > n3:
    print("O segundo número é maior")
elif n3 > n1 and n3 > n2:
    print("O terceiro número é maior")
else:
    print("Os número são iguais")