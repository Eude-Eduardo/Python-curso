dias_p = int(input("Quantos dias você ficou com o carro?"))
km_p = float(input("Quantos quilometros foram rodados nesses {} dias?".format(dias_p)))

dia = dias_p*60
km = km_p*0.15
res = dia+km

print("Valor total a pagar é de R${:.2f}".format(res))