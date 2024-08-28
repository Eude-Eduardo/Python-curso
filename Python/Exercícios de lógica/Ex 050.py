# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
num = 0
i = 0
quantP = quantI = 0
print("=="*20)
while i < 10:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        quantP += 1
    else:
        quantI += 1
    i += 1
print("=="*20)
print(
    f"Existem {quantP} números pares\n"
    f"e {quantI} números impares"
)
