num = []
res = ""
par = []
impar = []
while True:
    num.append(int(input("Digite um valor: ")))
    res = ""
    while True:
        res = str(input("Quer continuar? [S/N]")).strip().upper()[0]
        if res == "S" or res == "N":
            break
    if res == "N":
        break
for parImpar in num:
    if parImpar % 2 == 0:
        par.append(parImpar)
    else:
        impar.append(parImpar)
print("=="*20)
print(f"A lista completa é: {num}")
print(f"Os números pares são: {par}")
print(f"Os impares são: {impar}")