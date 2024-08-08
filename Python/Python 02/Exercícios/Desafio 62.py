inicio = int(input("Digite o inicio: "))
razão = int(input("Digite a razão: "))
i = 0
num = inicio
while i != 10:
    print(f"{num}", end="-> ")
    num += razão
    i += 1
    if i == 10:
        res = int(input("Quer mais termos? quantos: "))
        if res < 0:
            print("")
        else:
            while res != 0:
                print(f"{num}", end="-> ")
                num += razão
                res -= 1
print("FIM!")