from time import sleep
print("========== Lojas Eude's ==========")
val = float(input("Qual o valor total das compras? R$ "))
print("Escolha o método de pagamento")
print("""1- Dinheiro ou pix
2- Cartão"""
)
metP = int(input(""))
print("Processando ...")

sleep(1.5)

if metP == 1 or metP ==2:
    if metP == 1:
        print(f"O valor do pagamento em dinheiro/pix é R${val-(val*0.1):.2f}")
    else:
        print("Em quantas vezes")
        print("1- 1x/à vista")
        print("2- 2x")
        print("3- 3x ou mais")
        vz = int(input(""))
        if vz == 1:
            print(f"O valor do pagamento em 1x/à vista no cartão é {val-(val*0.05):.2f}")
        elif vz == 2:
            print(f"Será parcelado em 2x de R${val/2:.2f}, \n O valor total seria: R${val:.2f}")
        elif vz == 3:
            print("Quantas vezes? Max: 15")
            vz2 = int(input(""))
            if vz2 > 3 and vz2 <= 15:
                print(f"Será parcelado em {vz2}x de R${(val+(val*0.2))/vz2:.2f}, \n O valor total seria: R${val+(val*0.2):.2f}")
            elif vz2 <= 3 :
                print(f"valor inválido")
            else:
                print("Excedeu o número max de parcelas")
        else:
            print("Inválido")
else:
    print("Forma de pagamento inválida")