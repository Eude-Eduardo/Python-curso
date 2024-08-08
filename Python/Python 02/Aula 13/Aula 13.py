"""i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in  range(i, f+1, p):
    print(c)
print("Fim!")"""
s = 0
for c in range(0, 4):
    n = int(input("Digite um número: "))
    s += n
print(f"A soma de todos os valores {s}")