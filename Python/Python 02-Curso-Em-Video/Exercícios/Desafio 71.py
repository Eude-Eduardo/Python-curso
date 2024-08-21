print("=="*20)
print(f"{"BANCO":^40}")
print("=="*20)
saque = int(input("Que valor quer sacar? R$"))
nota50 = 50
nota20 = 20
nota10 = 10
nota1 = 1
quant50 = quant20 = quant10 = quant1 = 0

while True:
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
    if saque == 0:
        break
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


# Opção 2
print("=="*20)
print(f"{"BANCO":^40}")
print("=="*20)
saque = int(input("Que valor quer sacar? R$"))
total = saque
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced +=1
    else:
        if totalced > 0: 
            print(f"Total de {totalced} cédulas de R${ced:.2f}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print("Volte sempre")
