c = float(input("Digite a temperatura em ºC:"))
f = (c * 9 / 5) + 32
k = c + 273.15

print("A temperatura de {:.1f}ºC corresponde a {:.1f}ºF e {:.2f}K".format(c, f, k))