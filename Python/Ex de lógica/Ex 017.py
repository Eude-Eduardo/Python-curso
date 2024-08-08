import math

metro_quadrados = float(input("Digite as medidas da parede em m²: "))

rendimento_litro = 6
lata = 18 
custo_lata = 80
galao = 3.6
custo_galao = 25
rendimento_lata = rendimento_litro*lata
rendimento_galao = rendimento_litro*galao

somente_lata =  math.ceil(metro_quadrados / rendimento_lata)
somente_galao = math.ceil(metro_quadrados / rendimento_galao)
latas = math.floor(metro_quadrados*1.1/rendimento_lata)
galoes = math.ceil((metro_quadrados*1.1 % rendimento_lata)/ rendimento_galao)


print(f"Apenas latas: {somente_lata} custando R${somente_lata * custo_lata:.2f}")
print(f"Apenas galões {somente_galao} custando R${somente_galao * custo_galao:.2f}")
print(f"Latas: {latas}, Galões: {galoes}, custando {(latas * custo_lata)+(galoes*custo_galao):.2f}")