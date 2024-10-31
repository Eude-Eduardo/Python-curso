estado = dict()
brasil = list()
for c in range(0, 3):
    estado["UF"] = str(input("Unidade Federativa: "))
    estado["Sigla"] = str(input("Sigla do estado: "))
    brasil.append(estado.copy())
    print("-=" * 10)
for e in brasil:
    for k, v in e.items():
        print(f"{k}: {v}|", end=" ")
    print()