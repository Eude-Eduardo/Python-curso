num = []
n = res = 0
while True:
    n = int(input("Digite um valor: "))
    if num.count(n) == 0:
        print("Valor adicionado com sucesso...")
        num.append(n)
    else:
        print("Valor duplicado! não será adicionado")
    res = ""
    while res != "S" and res != "N":
        res = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if res == "N":
        break
print("=-="*15)
num.sort()
print(f"Você digitou os valores {num}")

