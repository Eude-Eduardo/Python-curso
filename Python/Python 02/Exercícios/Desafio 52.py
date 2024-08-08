num = int(input("Digite pra saber se é primo: "))
p = 0

for n in range(2, num +1):
    if num % n == 0:
        p += n
        if p > num:
            res = "Não é primo"
        elif p == num:
            res = "É primo"
if num == 1:
    print('O número 1 não é primo nem composto')
else:
    print(f"O número'{num}' {res}")