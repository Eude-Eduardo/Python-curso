print("DIGITE A DATA EM FORMATO dd/mm/aaaa")
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
if len(str(ano)) == 4:
    if mes > 12 or mes < 1:
        print(f"Mês inválido! você digitou o mês {mes:02} e só existe do mês 01 até o mês 12")
    else:
        if mes in [1,3,5,7,8,10,12]:
            if dia > 31 or dia < 1:
                print(f"Dia inválido! você digitou {dia} dias e o mês {mes:02} pode ter de 1 a 31 dias")
            else:
                print(f"{dia}/{mes:02}/{ano} registrado com sucesso!")
        else:
            if dia > 30 or dia < 1:
                print(f"Dia inválido! você digitou {dia} dias e o mês {mes:02} pode ter de 1 a 30 dias")
            else:
                print(f"{dia}/{mes:02}/{ano}  resgistrado com sucesso!")
else:
    print("Ano inválido!")
