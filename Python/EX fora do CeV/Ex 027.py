n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

if n1 > n2 and n2 > n3:
    print(f"Em ordem decrescente fica: {n1} {n2} {n3}")
elif n2 > n1 and n1 > n3:
    print(f"Em ordem decrescente fica: {n2} {n1} {n3}")
elif n3 > n1 and n1 > n2:
    print(f"Em ordem decrescente fica: {n3} {n1} {n2}")
elif n1 > n2 and n2 < n3:
    print(f"Em ordem decerescente fica: {n1} {n3} {n2}")
elif n3 > n2 and n2 > n1:    
    print(f"Em ordem decrescente fica: {n3} {n2} {n1}")
elif n2 > n3 and n3 > n1:
    print(f"Em ordem decrescente fica: {n2} {n3} {n1}") 
else:    
    print("MAIS?")
