sx = []
nm = ""
id = 0
res = []
for md in range(1, 5):
    print(f"------ {md}ª Pessoa ------")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    id += idade
    if sexo.lower() == "m":
        sx.append(idade)
        if idade == max(sx):
            nm = nome.capitalize()
    elif sexo.lower() == "f":
        if idade < 20:
            res.append(nome)
    else:
        print("Sexo inválido")
print(
    f"A média de idade do grupo é de {id/4} \n"
    f"O homem mais velho tem {max(sx)} anos e se chama {nm}\n"
    f"Ao todo são {len(res)} mulheres com menos de 20 anos"

)    
    
    