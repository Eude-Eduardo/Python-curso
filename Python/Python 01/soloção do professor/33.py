n1 = int(input("1º Valor:"))
n2 = int(input("2º Valor:"))
n3 = int(input("2º Valor:"))
# verificando Menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando Maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")
