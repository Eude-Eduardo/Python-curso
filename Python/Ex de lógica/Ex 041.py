"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

# 80000 3%/ano
# 20000 1.5%/ano
# anos para que A >= B

habitanteA = 80000
habitanteB = 200000
taxaA = 0.03
taxaB = 0.015
cont = 0

while habitanteA < habitanteB:
    habitanteA += habitanteA * taxaA
    habitanteB += habitanteB * taxaB
    cont +=1

print(f"Serão {cont} anos para que a população A passe a população B")