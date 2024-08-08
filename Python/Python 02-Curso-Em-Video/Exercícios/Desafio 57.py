sexo = ""
nome = str(input('Seu nome: ')).strip()
print(f"Seu nome {nome.capitalize()} foi registrado com sucesso!")
while sexo != "F" and sexo != "M":
    sexo = str(input("Seu sexo [F/M]: ")).upper()[0].strip()
    if sexo != "F" and sexo !="M":
        print("Sexo inválido! Digite Novamente. ")
if sexo == "F":
    sx = "Feminino"
else:
    sx = "Masculino"

print(f"Seu sexo '{sx}' foi registrado com sucesso!")