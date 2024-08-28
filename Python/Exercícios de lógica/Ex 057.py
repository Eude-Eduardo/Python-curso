# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Digite um número para saber se ele é primo: "))
primo = 0
if num == 1:
    print("o número 1 não é composto e nem considerado um número primo")
else:
    for c in range(1, num+1):
        if num % c == 0:
            primo += 1
        if primo == 2:
            res = 'é primo'
        else:
            res = "não é primo"
    print(f"O número {num} {res}")