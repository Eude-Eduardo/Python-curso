p1 = float(input("digite o preço do primeiro produto: R$")) 
p2 = float(input("digite o preço do segundo produto: R$"))
p3 = float(input("digite o preço do terceiro produto: R$"))

if p1 < p2 and p1 < p3:
    print(f"O primeiro produto com o preço de R${p1:.2f} é o mais barato")
elif p2 < p1 and p2 < p3:
    print(f"O segundo produto com o preço de R${p2:.2f} é o mais barato")
elif p3 < p1 and p3 < p2:
    print(f"O terceiro produto com o preço de R${p3:.2f} é o mais barato")
elif p1 == p2 and p1 == p3:
    print(f"Os 3 produtos te preços iguais")
elif p1 > p2 == p3:
    print(f"Os produtos 2 e 3 tem o mesmo preço e são mais baratos, preço: R${p2:.2f}")
elif p2 > p1 == p3:
    print(f"Os produtos 1 e 3 tem o mesmo preço e são mais baratos, preço: R${p1:.2f}")
elif p3 > p1 == p2 :
    print(f"Os produtos 1 e 2 tem o mesmo preço e são mais baratos, preço: R${p3:.2f}")
else:
    print("ERRO!")