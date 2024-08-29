sinais = ["(",")"]
ex = str(input("Digite a expressão: "))
valid = []
for letra in ex:
    if letra in sinais:
        valid.append(letra)

if len(valid) == 0:
    res = "não tem parenteses"        
elif len(valid) == 1:
    res = "não é válida"
else:
    if valid.count("(") == valid.count(")"):
        res = "é valida"
    else:
        res = "não é válida"
print(f"A expressão {res}")