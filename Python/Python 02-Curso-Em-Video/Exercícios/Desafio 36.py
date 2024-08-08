val_house = float(input("Qual o valor da casa? R$"))
sal = float(input("Qual o seu salário? R$"))
par = int(input("Quantos anos de financiamento?"))
tempo = par * 12
p = val_house / tempo 

if p <= sal*0.3:
    print(f"Uma casa de R${val_house:.2f} e o valor das suas parcelas será de R${p:.2f}")
else:
    print(f"Uma casa de R${val_house:.2f} e o valor das suas parcelas será de R${p:.2f}")
    print("Lamento mas o seu empréstimo foi negado.")