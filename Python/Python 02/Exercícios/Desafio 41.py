from datetime import date

dia = int(input("Que dia você nasceu?"))
mes = int(input("Que mês você nasceu?"))
ano = int(input("Que ano você nasceu?"))
Dat = date.today().day
Mat = date.today().month
Aat = date.today().year

if mes < Mat:
    id = Aat - ano
elif dia <= Dat:
    id = (Aat - ano)-1
else:
    id = (Aat - ano)-1

if id < 0:
    print("Idade Inválida")
elif id <= 9:
    print(f"Com {id} anos você faz parte da categoria Mirim")
elif id <= 14:
    print(f"Com {id} anos você faz parte da categoria Infantil")
elif id <= 19:
    print(f"Com {id} anos você faz parte da categoria Junior")
elif id <= 20:
    print(f"Com {id} anos você faz parte da categoria Sênior")
else:
    print(f"Com {id} anos você faz part da categoria Master")
