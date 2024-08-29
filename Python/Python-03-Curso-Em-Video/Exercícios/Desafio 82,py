num = []
res = ""
while True:
    num.append(int(input("Digite um valor: ")))
    res = ""
    while True:
        res = str(input("Quer continuar? [S/N]")).strip().upper()[0]
        if res == "S" or res == "N":
            break
    if res == "N":
        break
par = []
impar = []
for parImpar in num:
    if parImpar % 2 == 0:
        par.append(parImpar)
    else:
        impar.append(parImpar)
print("A lista completa é: ", end="")
for n in num:
    print(n, end=". ")
print("\nOs números pares são: ",end="")
for p in par:
    print(p, end=". ")
print("\nOs impares são: ", end="")
for i in impar:
    print(i, end=". ")