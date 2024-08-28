num = float(input("Digite uma nota entre 0 e 10: "))
while num < 0 or num > 10:
    num = float(input("inválido! Por favor digite novamente:"))
print(f"{num} registrado com sucesso")