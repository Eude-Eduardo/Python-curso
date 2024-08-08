inicio = int(input("Digite o inicio: "))
razão = int(input("Digite a razão: "))
i = 0
num = inicio
while i != 10:
    print(f"{num}", end="-> ")
    num += razão
    i += 1
print("FIM!!")