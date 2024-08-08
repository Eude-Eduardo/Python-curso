opc = 0
while opc != 5:
    valor1 = int(input("Digite um número: "))
    valor2 = int(input("Digite outro número: "))
    print(
        "O que você vai querer fazer com eles?\n"
        "[1] Somar\n"
        "[2] Multiplicar\n"
        "[3] Maior\n"
        "[4] Novos números\n"
        "[5] Sair do programa"    )
    opc = int(input(""))
    if opc == 1:
        print(f"A soma de {valor1} + {valor2} = {valor1+valor2}")
    elif opc == 2:
        print(f"{valor1} x {valor2} = {valor1*valor2}")
    elif opc == 3:
        if valor1 > valor2 :
            print(f"O número {valor1} é maior que {valor2}")
        elif valor2 > valor1:
            print(f"O número {valor2} é maior que {valor1}")
        else:
            print(f"Os dois números são iguais")
print("-=-ENCERRADO-=-")