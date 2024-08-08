n = str(input("Digite seu nome completo:"))
nome = n.split()
print("Prazer em te conhecer {}!".format(n))
print("Seu primeiro nome é {}".format(nome[0].capitalize()))
print("Seu ultimo nome é {}".format(nome[len(nome)-1].capitalize()))

