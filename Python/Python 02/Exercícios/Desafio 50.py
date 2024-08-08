soma = 0
conta = 0
for c in range(1, 7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
        conta += 1
print(f"E a soma entre todos os {conta} números pares é {soma}")