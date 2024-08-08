cont = 0
num = []
res = "S"
while res == "S":
    num.append(int(input("Digite um número: ")))
    res = str(input("Quer continuar [S/N]: ")).upper()
    cont += 1
print(f"Você digitou {cont} números e a média foi {sum(num)/cont}")
print(f"o maior valor foi {max(num)} e o menor foi {min(num)}")
