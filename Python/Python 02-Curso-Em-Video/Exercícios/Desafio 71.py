print("=="*20)
print(f"{"BANCO":^40}")
print("=="*20)
saque = int(input("Que valor quer sacar? R$"))
nota50 = 50
nota20 = 20
nota10 = 10
nota1 = 1
quant50 = quant20 = quant10 = quant1 = 0

while saque > 0:
    if saque - nota50 >= 0:
        saque -= nota50
        quant50 += 1
    elif saque - nota20 >= 0:
        saque -= nota20
        quant20 += 1 
    elif saque - nota10 >= 0:
        saque -= nota10
        quant10 += 1
    elif saque - nota1 >= 0:
        saque -= nota1
        quant1 += 1
print("=="*20)
if quant50 > 0:
    print(f"Total de {quant50:2} notas de R$50,00")
if quant20 > 0:
    print(f"Total de {quant20:2} notas de R$20,00")
if quant10 > 0:
    print(f"Total de {quant10:2} notas de R$10,00")
if quant1 > 0:
    print(f"Total de {quant1:2} notas de R$1,00 ")

print("=="*20)
print("Volte Sempre! Tenha um bom dia!")

    