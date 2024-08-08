from datetime import date
Anoat = date.today().year
maior = 0
menor = 0
for perg in range(1, 8):
    ano = int(input(f"Em que ano a {perg}ª Nasceu? "))
    if  Anoat - ano <= 21:
        menor += 1
    else:
        maior += 1            
print(f"{maior} Pessoas já atingiram a maioridade")
print(f"{menor} Pessoas ainda não atingiram a maioridade")
