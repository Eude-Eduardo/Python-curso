print("_="*23)
print("Digite dois valores para saber qual é maior")
print("_="*23)
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))

if n1 > n2:
    print(f"O valor {n1} é maior que {n2} (O primeiro valor é maior)")
elif n1 == n2:
    print(f"Não existe valor maior {n1} é igual a {n2}")
else:
    print(f"O Valor {n2} é maior que {n1} (O segundo valor é maior)")