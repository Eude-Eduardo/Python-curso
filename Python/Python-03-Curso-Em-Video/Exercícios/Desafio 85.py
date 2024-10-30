parImp = [[],[]]
for c in range(1, 8):
    num = int(input(f"Digite o {c}º valor: "))
    if num % 2 == 0:
        parImp[0].append(num)
    else:
        parImp[1].append(num)
print("-="*20)
parImp[0].sort()
parImp[1].sort()
print(f"Os valores pares digitados foram: {parImp[0]}")
print(f"os Valores impares digitados foram:{parImp[1]}")
