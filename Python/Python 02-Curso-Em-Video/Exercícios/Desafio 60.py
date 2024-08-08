num = int(input("Digite um número: "))
fac = num 
i = 1
n = num-1
while i != num:
    print(n)
    n -= 1
    fac += fac* n
    i += 1

print(f"O resultado de {num}! (fatorial) é {fac}")
