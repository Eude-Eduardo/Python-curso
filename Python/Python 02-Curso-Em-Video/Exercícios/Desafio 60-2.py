num = int(input("Digite um número: "))
fatorial = num
for c in range(num-2, 0, -1):
    fatorial += fatorial*c
print(f"o resultado de {num}! é {fatorial}")
