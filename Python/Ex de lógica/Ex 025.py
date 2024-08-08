n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: ")) 

if n1 > n2:
    print("o maior é o primeiro")
    if n2 < n3:
        print("O segundo é menor")
    else:
        print("O terceiro é menor")
elif n2 > n1 and n2 > n3:
    print("O segundo é maior")
    if n1 < n3:
        print("O primeiro é menor")
    else:
        print("O terceiro é menor")
elif n3 > n1 and n3 > n2:
    print("O maior é o terceiro")
    if n2 < n1:
        print("o segundo é menor")
    else:
        print("O Primeiro é menor")
else:
    print("Pelo menos dois valores são iguais")