alt = float(input("Qual a sua altura em Metros:"))
print("Qual o seu gênero(Biologico):")
print("""1- Masculino
2- Feminino""")
gen = int(input(""))
peso_homens = (72.7*alt)-58
peso_mulheres = (62.1*alt)-44.7

if gen == 1:
    print(f"Seu peso ideal seria {peso_homens:.2f}Kg")
elif gen == 2:
    print(f"Seu peso ideal seria {peso_mulheres:.2f}Kg")
else:
    print("Valor de gênero errado digite 1 ou 2")