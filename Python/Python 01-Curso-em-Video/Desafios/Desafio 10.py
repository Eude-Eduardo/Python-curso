din = float(input("Digite quanto você tem: R$"))
dol = din/5.51
eur = din/5.89
print("Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}".format(din,dol,eur))