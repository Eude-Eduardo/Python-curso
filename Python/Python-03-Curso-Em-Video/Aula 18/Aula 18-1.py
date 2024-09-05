teste = list()
pessoas = list()
teste.append("Gustavo")
teste.append(40)
pessoas.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
pessoas.append(teste[:])
print(pessoas)