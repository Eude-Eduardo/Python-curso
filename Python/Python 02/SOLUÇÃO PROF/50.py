soma = 0
for c in range(1, 7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
print(f"E a soma entre todos os números pares é {soma}")