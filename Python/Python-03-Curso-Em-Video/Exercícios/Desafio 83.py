expr = str(input("Digite a exprpressão: "))
valid = []
for letra in expr:
    if letra in "()":
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
print(f"A exprpressão {res}")