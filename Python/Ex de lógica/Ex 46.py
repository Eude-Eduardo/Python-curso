# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles
num = int(input("Digite um número: "))
numFinal =  int(input("Didigte outro número: "))

while num < numFinal-1:
    num += 1
    print(f"{num}", end="➱  ")
print("FIM!")