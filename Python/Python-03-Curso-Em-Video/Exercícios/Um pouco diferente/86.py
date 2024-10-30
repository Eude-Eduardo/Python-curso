matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f"Difgite um valor para [{i}, {c}]: "))
print("-="*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()