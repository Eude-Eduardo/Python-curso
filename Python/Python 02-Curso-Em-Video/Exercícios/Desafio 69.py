res = "S"
sexo = ""
idade = 0
cont18 = 0
contH = 0
contM20 = 0
while res == "S":
    print("--"*12)
    print("Cadastre uma pessoa")
    print("--"*12)
    idade = int(input("Idade: "))
    sexo = str(input("sexo: [M/F] ")).upper()[0]
    while sexo != "M" and sexo != "F":
        sexo = str(input("sexo: [M/F] ")).upper()[0]
    if sexo == "F":
        if idade < 20:
            contM20 += 1
        if idade >= 18:
            cont18 += 1
    else:
        contH += 1
        if idade >= 18:
            cont18 += 1
    res = str(input("Quer continuar?: [S/N] ")).upper()[0]
    while res != "S" and res != "N":
        res = str(input("Quer continuar?: [S/N] ")).upper()[0]
print("===FIM DO PROGRAMA===")
    
print(
    f"Total de pessoas com mais de 18 anos: {cont18} \n"
    f"Ao todo temos {contH} homens cadastrados \n"
    f"E temos {contM20} mulheres com menos de 20 anos"
)