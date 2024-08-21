quant18 = quantHomens = quantMulheresMenos20 = 0

while True:
    print("--"*12)
    print("Cadastre uma pessoa")
    print("--"*12)
    idade = int(input("Idade: "))
    sexo = ""
    while sexo != "M" and sexo != "F":
        sexo = str(input("sexo: [M/F] ")).upper()[0].strip()
    if idade >= 18:
            quant18 += 1
    if sexo == "F":
        if idade < 20:
            quantMulheresMenos20 += 1
    else:
        quantHomens += 1
    res = " "
    while res != "S" and res != "N":
        res = str(input("Quer continuar?: [S/N] ")).upper()[0].strip()
    if res == "N":
        break
print("===FIM DO PROGRAMA===")
    
print(
    f"Total de pessoas com mais de 18 anos: {quant18} \n"
    f"Ao todo temos {quantHomens} homens cadastrados \n"
    f"E temos {quantMulheresMenos20} mulheres com menos de 20 anos"
)