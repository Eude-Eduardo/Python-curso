# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
num = int(input("Digite um número para saber o fatorial: "))
n = num
for c in range(2, num):
    n *= c
print(f"{n}")