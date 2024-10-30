spar = mai = scol = 0
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
for n in range(0, 3):
    for l in range(0,3):
        print(f"[ {matriz[n][l]:^5} ]", end="")
        if matriz[n][l] % 2 == 0:
            spar += matriz[n][l]
    print()
print(f"A soma dos valores pares é {spar}")
for l in range(0, 3):
    scol += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {scol}")
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f"O maior valor da segunda linha é {mai}")
