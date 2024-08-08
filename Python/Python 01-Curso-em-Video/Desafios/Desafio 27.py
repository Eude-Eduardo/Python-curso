name = str(input("qual seu nome completo?")).strip()
n = name.split()

print("seu nome é {}".format(name))
print("Primeiro nome é {}".format(n[0].capitalize()))
print("Seu ultimo nome é {}".format(n.pop().capitalize()))


