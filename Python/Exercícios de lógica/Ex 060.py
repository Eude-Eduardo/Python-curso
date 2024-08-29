# Faça um programa que calcule o mostre a média aritmética de N notas.
num = quant = soma =  cont = 0
res = ""
while True:
    num = float(input("Digite a nota: "))
    while num < 0 or num > 10:
        num = float(input("Nota inválida. Digite novamente: "))
    soma += num
    quant += 1
    cont += 1
    if cont == 4:
        res = ""
        while res != "S" and res != "N":
            res = str(input("Mais notas? [S/N]")).strip().upper()[0]
        cont = 0
    if res == "N":
        break
print(f"A média da {quant} notas é {soma/quant}")