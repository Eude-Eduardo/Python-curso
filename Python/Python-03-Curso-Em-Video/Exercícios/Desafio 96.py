def frescurasVisuais(título):
    print()
    print(f"{título:^30}")
    print("-=" * 15)
def area(l, c):
    print(f"A area do terreno {l}x{c} é de {l * c}m².")


frescurasVisuais("Controle de Terrenos")
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)