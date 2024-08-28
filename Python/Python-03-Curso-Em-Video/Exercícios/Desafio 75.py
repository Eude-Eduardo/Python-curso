num = (int(input("Digite um número: ")),int(input("Digite outro número: ")) ,int(input("Digite mais um número: ")) ,int(input("Digite o último número: ")))

print(f"Você digitou os valores: {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if num.count(3) == 0:
    print("O valor 3 não apareceu em nenhuma posição")
else:
    print(f"O número 3 apareceu na {num.index(3)+1}ª posição")
print(f"Os valores pares digitados: ", end="")

for c in num:
    if c % 2 == 0:
        print(c, end=" ") 