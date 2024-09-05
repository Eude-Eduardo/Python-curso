"""pessoas = [["Eude", 20],["Ana", 19],["joaquin", 13],['Maria', 45]]
for p in pessoas:
    print(f"{p[0]} tem {p[1]} anos")"""
pessoas = list()
dadosTemp = list()
for c in range(0, 3):
    dadosTemp.append(str(input('Nome: ')))
    dadosTemp.append(str(input("Idade: ")))
    pessoas.append(dadosTemp[:])
    dadosTemp.clear()
print(pessoas)