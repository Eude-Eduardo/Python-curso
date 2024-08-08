# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite um ano para saber se é bissexto: "))

if ano % 100 == 0:
    if ano % 400 == 0:
        print(f"O ano {ano} é bissexto.")
    else:
            print(f"O ano {ano} não é bissexto.")
elif ano % 4 == 0:
     print(f"O ano {ano} é bissexto.")
else:
     print(f"O ano {ano} não é bissexto.")
