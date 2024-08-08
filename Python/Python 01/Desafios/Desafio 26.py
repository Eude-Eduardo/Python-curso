frase = str(input("digite uma frase:")).strip()
a1=frase.lower().count("a")
a2=frase.lower().find("a")
a3=frase.lower().rfind("a")

print("A letra a aparece {} vezes".format(a1))
print("A a parece pela primeira vez na posição {}".format(a2+1))
print("e a ultima na posição {}".format(a3+1))

