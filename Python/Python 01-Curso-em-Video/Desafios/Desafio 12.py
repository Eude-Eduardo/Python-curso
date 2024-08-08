pr = float(input("Qual o preço do produto? R$"))
des = pr-(pr*0.05)
print("O valor de R${:.2f} com 5% de desconto é R${:.2f}".format(pr, des))