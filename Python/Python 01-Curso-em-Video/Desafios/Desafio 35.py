print("__==__"*8)
print("Analizador de Triângulos")
print("__==__"*8)

r1 = float(input("Reta 1:"))
r2 = float(input("Reta 2:"))
r3 = float(input("Reta 3:"))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print("Os segmentos PODEM formar um triângulo")
else:
    print("Os segmentos NÃO PODEM formar um triângulo")