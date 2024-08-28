# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
soma = cont = menor = maior = num = 0

while True:
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    elif num < menor:
        menor = num
    elif num > maior:
        maior = num
    res = " "
    while res not in "SN":
        res = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if res == "N":
        print("{:=^40}".format("FIM DO PROGRAMA"))
        break
print(
    f"O Maior é {maior}\n"
    f"O Menor é {menor}\n"
    f"A soma dos valores é {soma}"  
    )
    