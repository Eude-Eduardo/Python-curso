def escreva(txt):
    l = len(txt) + 4
    print("~" * l)
    print("{:^{}}".format(txt, l))
    print("~" * l)


escreva("Centralizado e Adaptado")