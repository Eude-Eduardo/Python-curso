num = int(input("Digite um número: "))
fatorial = num
ft = 1
print(f"calculando {num}!, ")
while fatorial > 0:
    print(f"{fatorial}", end="")
    print(f" x " if fatorial > 1 else " = ", end="")
    ft *= fatorial
    fatorial -= 1
print(f"{ft}")

1969
