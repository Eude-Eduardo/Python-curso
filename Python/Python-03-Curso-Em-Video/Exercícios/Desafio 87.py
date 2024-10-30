matriz = [[],[],[]]
for c in range(0, 3):
    for m in range(0 ,3):
        num = int(input(f"Digite um valor para [{c}, {m}]: "))
        if c == 0: 
            matriz[0].append(num)
        elif c == 1:
            matriz[1].append(num)
        else:
            matriz[2].append(num)
print("=="*20)
for n in matriz[0]:
    print(f"[ {n:^3} ]", end=" ")
print()
for number in matriz[1]:
    print(f"[ {number:^3} ]", end=" ")
print()
for numero in matriz[2]:
    print(f"[ {numero:^3} ]", end=" ")
print()
print("=="*20)
par = list()
imp = list()
for i in matriz:
    for parImpar in i:
        if parImpar % 2 == 0:
            par.append(parImpar)
        else:
            imp.append(parImpar)
print(f"A soma dos valores pares é {sum(par)}.")
print(f"A soma dos valores das terceira coluna {matriz[0][2] + matriz[1][2] + matriz[2][2]}.")
print(f"o maior valor da segunda linha é {max(matriz[1])}.")