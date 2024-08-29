numbers = list()

for c, n in enumerate(range(0, 5)):
    numbers.append(int(input(f'Digite um valor para a posição {c}: ')))
print("Você digitou os valores: ", end="")
for p, num in enumerate(numbers):
    print(f"{num}", end=", "if p != 4 else ".")

print(f"\nO maior valor digitado foi {max(numbers)} nas posições ", end="")
for pos, v in enumerate(numbers):
        if v == max(numbers):
            print(pos, end="...")
print(f"\nO menor valor digitado foi {min(numbers)} nas posições ", end="")
for posicao, val in enumerate(numbers):
    if val == min(numbers):
        print(posicao, end="...")

