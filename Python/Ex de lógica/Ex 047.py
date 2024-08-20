# Altere o programa anterior para mostrar no final a soma dos números
num = int(input("Digite um número: "))
numFinal =  int(input("Didigte outro número: "))
n = num
soma = 0
while num < numFinal-1:
    num += 1
    print(f"{num}", end="➱  ")
    soma += num
print("FIM!")
print(
    f"A soma dos valores entre os números digitados : {soma}\n"
    f"A soma dos valores incluindo os digitados: {soma+n+numFinal}\n"
    f"A soma apenas dos digitatos: {n+numFinal}\n"
    )
