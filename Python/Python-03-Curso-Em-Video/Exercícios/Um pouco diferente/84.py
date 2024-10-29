temp = []
princ = []

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp [:])
    temp.clear()
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break
print("-=" * 30)
print(f"Ao todo Você cadastrou {len(princ)} pessoas")
print(f"O maior peso foi de {mai}Kg. Peso de ", end="")
for pos,p in enumerate(princ):
    if p[1] == mai:
        print(f"{p[0]}", end="." if pos == len(princ)-1 else ", ")
print(f"\nO menor peso foi de {men}kg.Peso de ", end="" )
for pp, i in enumerate(princ):
    if i[1] == men:
        print(f"{i[0]}", end=". " if pp == len(princ)-1 else ".")