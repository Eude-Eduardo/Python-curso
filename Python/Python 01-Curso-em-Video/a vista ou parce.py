preço = float(input("Qual o preço original? R$"))
vista = preço - (preço*10/100)
parce = preço + (preço*8/100)

print("Um produto de R${:.2f}, a vista com desconto de 10% custa R${:.2f} mas parcelado no cartão tem um aumento de 8% fica po R${:.2f}".format(preço, vista, parce))