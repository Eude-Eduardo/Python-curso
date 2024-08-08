num = int(input("Digite pra saber se é primo: "))
tot = 0

for n in range(1, num +1):
    if num % n == 0:
        print("\033[32m", end=" ")
        tot += 1
        if tot > 2:
            res = "Não é primo"
        elif tot == 2:
            res = "é primo"
    else:
        print("\033[33m", end=" ")
    print(f"{n}", end=" ")

if num == 1:
    print('O número 1 não é primo nem composto')
else:
    print(f"\n \033[mO número {num} foi dividido {tot} vezes")
    print(f"O número '{num}' {res}")