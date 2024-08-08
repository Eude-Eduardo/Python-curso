nome = str(input("Qual é o seu nome?")).lower()
if nome == "eude":
    print(f"Que nome lindo {nome.title()}")
elif nome == "maria" or nome == "paulo" or nome == "pedro":
    print(f"Seu nome é bem comum no Brasil {nome.title()}")
elif nome in "ana jessica paula fabiana":
    print(f"Belo nome feminino {nome.title()}")
print(f"Tenha um bom dia {nome.title()}")