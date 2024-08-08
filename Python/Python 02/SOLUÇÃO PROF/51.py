print("=="*18)
print("          10 Termos de PA")
print("=="*18)

inicio = int(input("Inicio: "))
passo = int(input("Razão: "))
dec = inicio + (10-1) * passo
for c in range (inicio, dec+passo, passo):
    print(f"{c}", end="-> ")
print("Acabou!")
