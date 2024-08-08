import math

'''num = float(input("Digite um número:"))'''

#Maneira que eu fiz--

'''print("O número {} tem a parte inteira {}".format(num,math.floor(num) ))'''

#maneiras do professor

num = float(input("Digite um número:"))

#print("A parte inteira do número {} é {}".format(num, int(num)))

print("O número {} tem a parte inteira {}".format(num,math.trunc(num) ))

