import math

metros_quadrados = float(input("Digite os m²: "))
metros_quadrados_mais_dez = metros_quadrados * 1.0

rendimento_litro = 6
litros_lata = 18
preco_lata = 80
rendimento_lata = rendimento_litro * litros_lata
litros_galao = 3.6
preco_galao = 25
rendimento_galao = rendimento_litro * litros_galao

somente_latas = math.ceil(metros_quadrados / rendimento_lata)
somente_galoes = math.ceil(metros_quadrados / rendimento_galao)
latas = math.floor(metros_quadrados_mais_dez / rendimento_lata)
galoes = math.ceil(
    (metros_quadrados_mais_dez % rendimento_lata) / rendimento_galao
)

print(
    f"Somente Latas: {somente_latas}, "
    f"custando R${somente_latas * preco_lata}\n"
    f"Somente Galões: {somente_galoes}, "
    f"custando R${somente_galoes * preco_galao}\n"
    f"Latas: {latas} , Galões: {galoes}, "
    f"custando R${((latas * preco_lata) + (galoes *preco_galao)):.2f}"
)