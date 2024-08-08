n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro valor:"))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2

print("a soma vale {}, \n a multiplicação vale {}, \n a divisão vale {:.3f} ".format(s, m, d), end=" ")

print("A divisão inteira vale {} e a potencia é {}".format(di, p))

