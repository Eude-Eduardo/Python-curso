year = int(input("digite um ano para saber se ele é bissexto:"))
if year % 100 == 0:
    if year % 400 == 0:
        print(f"O ano de {year} é bissexto")
    else:
        print(f"O ano de {year} não é bissexto")
else:
    if year % 4 == 0:
        print(f"O Ano de {year} é bissexto")        
    else:
        print(f"O ano de {year} não é bissexto")