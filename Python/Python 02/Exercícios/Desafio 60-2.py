num = int(input("Digite um número: "))
fac = num
for c in range(num-2, 0, -1):
    print(c)
    print(fac)
    fac += fac*c
print(f"o resultado de {num}! é {fac}")