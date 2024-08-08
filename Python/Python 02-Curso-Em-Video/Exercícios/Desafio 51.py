inicio = int(input("Inicio: "))
passo = int(input("Razão: "))
dec = inicio + (10-1) * passo
for c in range (inicio, dec+passo, passo):
    print(f"{c}", end="-> ")
print("Acabou!")
