name = str(input('qual o seu nome:'))
n=name.lower()

print("o seu nome é {}".format(name))

if(n.find('silva') == -1 ):
    print("Você tem não silva no nome")
else:
    print("Você tem silva no nome")

