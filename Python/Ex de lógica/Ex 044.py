# Faça um programa que leia 5 números e informe a soma e a média dos números.
num = 0 
soma = 0
i = 0
while i < 5:
    num = int(input("Digite um número: "))
    soma += num
    i += 1
print(f"A soma dos valores é {soma} e a média é {soma/5}")