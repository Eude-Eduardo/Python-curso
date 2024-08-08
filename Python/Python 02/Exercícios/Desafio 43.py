alt = float(input("Qual sua altura em metros? (M) "))
peso = float(input("Qual seu peso em quilos? (Kg) " ))
alt = alt/100
imc = peso/(alt**2)

print(f"O seu IMC é {imc:.1f}")

if imc <= 17:
    print(f"Você está muito abaixo do peso")
elif imc <= 18.5:
    print(f"Você está abaixo do peso")
elif imc <= 24.9:
    print(f"Você está com o peso normal")
elif imc <= 29.9:
    print(f"Você está acima do peso normal")
elif imc <= 34.9:
    print(f"Você está com obesidade ")
elif imc <= 39.9:
    print(f"Você está obesidade severa")
else:
    print(f"Você está obesidade morbida")    