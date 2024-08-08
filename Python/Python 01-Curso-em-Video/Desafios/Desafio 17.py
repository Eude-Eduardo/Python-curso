import math

#maneira sem ver a aula

'''l1 = float(input("Digite o cateto oposto:"))
l2 = float(input("Digite o cateto adjacente:"))
h = math.sqrt(l1**2 + l2**2)

print("Um triangulo retângulo de lado com cateto oposto de {:.2f}cm e cateto adjacente de {:.2f}cm a hipotenusa tem {:.2f}cm".format(l1, l2, h))'''

#maneira da aula

l1 = float(input("Digite o cateto oposto:"))
l2 = float(input("Digite o cateto adjacente:"))
hi = math.hypot(l1,l2)

print("Um triangulo retângulo de lado com cateto oposto de {:.2f}cm e cateto adjacente de {:.2f}cm a hipotenusa tem {:.2f}cm".format(l1, l2, hi))

