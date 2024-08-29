num = []
res = 0
while True:
    num.append(int(input("Digite um valor: ")))
    res = ""
    while True:
        res = str(input("Quer continuar? [S/N]")).strip().upper()[0]
        if res == "S" or res == "N":
            break
    if res == "N":
        break
print("=="*20)
print(f"você digitou os valores: {num}")
print("=="*20)
print(f"Existem {len(num)} números nesta lista.")
print("=="*20)
n = num[:]
n.sort(reverse=True)
print(f"Os números em ordem decrescente são {n}.")
print("=="*20)
if num.count(5) == 0:
    print(f"Não existe número 5 nessa lista.")
else:
    print(f"O número 5 está na posição {n.index(5)+1} na ordem decrescente ou {num.index(5)+1} na lista comum.")