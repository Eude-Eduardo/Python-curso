"""num = int(input("Digite um número até 9999:"))
n1 =str(num)
n= n1.zfill(4)

if(num > -0 and num < 10000):
    print(f'Unidade:{n[3]}')
    print(f'dezena:{n[2]}')
    print(f'Centena {n[1]}')
    print(f'Milhar:{n[0]}')
else:
    print("número inválido")"""

#pf

num = int(input("Informe um número:"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("analisando o número".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("milhar: {}".format(m))