name = str(input("What's your name? "))
print("Em que turno você estuda?")
print("""[M] Matutino
[V] Vespertino
[N] Noturno""")
esc = input("Sua resposta: ").lower()

if esc == "m":
    print(f"Bom dia {name.capitalize()}!")
elif esc == "v":
    print(f"Boa tarde {name.capitalize()}!")
elif esc == "n":
    print(f"Boa noite {name.capitalize()}!")
else:
    print("Valor Inválido!")