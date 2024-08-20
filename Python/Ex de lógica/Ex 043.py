# Faça um programa que leia 5 números e informe o maior número
num =0
i = 0
cont = 0
maior = menor = 0
while i < 5:
    num = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    i += 1
print(f"O maior número é o {maior} e o menor é {menor}")