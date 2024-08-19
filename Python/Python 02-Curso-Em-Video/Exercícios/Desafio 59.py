from time import sleep
opçao = 0
valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))
while opçao != 5:
    print(
        "O que você vai querer fazer com eles?\n"
        "[1] Somar\n"
        "[2] Multiplicar\n"
        "[3] Maior\n"
        "[4] Novos números\n"
        "[5] Sair do programa"    )
    opçao = int(input(">>>>>>"))
    if opçao == 1:
        print(f"A soma de {valor1} + {valor2} = {valor1+valor2}")
        sleep(1)
    elif opçao == 2:
        print(f"{valor1} x {valor2} = {valor1*valor2}")
        sleep(1)
    elif opçao == 3:
        if valor1 > valor2 :
            print(f"O número {valor1} é maior que {valor2}")
            sleep(1)
        elif valor2 > valor1:
            print(f"O número {valor2} é maior que {valor1}")
            sleep(1)
        else:
            print(f"Os dois números são iguais")
            sleep(1)
    elif opçao == 4:
        valor1 = int(input("Digite um número: "))
        valor2 = int(input("Digite outro número: "))
    elif opçao != 5:
        print("inválido")
        sleep(1)
    print("=-="*12)
print("-=-ENCERRADO-=-")