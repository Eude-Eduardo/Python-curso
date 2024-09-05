matrix = [[],[],[]]
for c in range(0, 3):
    for m in range(0 ,3):
        num = int(input(f"Digite um valor para [{c}, {m}]: "))
        if c == 0: 
            matrix[0].append(num)
        elif c == 1:
            matrix[1].append(num)
        else:
            matrix[2].append(num)
print("=="*20)
for n in matrix[0]:
    print(f"[ {n} ]", end=" ")
print()
for number in matrix[1]:
    print(f"[ {number} ]", end=" ")
print()
for numero in matrix[2]:
    print(f"[ {numero} ]", end=" ")
print()
print("=="*20)
par = list()
imp = list()
for i in matrix:
    for parImpar in i:
        if parImpar % 2 == 0:
            par.append(parImpar)
        else:
            imp.append(parImpar)
print(f"A soma dos valores pares é {sum(par)}.")
print(f"A soma dos valores das terceira coluna {matrix[0][2] + matrix[1][2] + matrix[2][2]}.")
print(f"o maior valor da segunda linha é {max(matrix[1])}.")