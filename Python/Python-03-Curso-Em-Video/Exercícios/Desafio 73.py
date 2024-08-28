times = ("Fortaleza","Botafogo","Palmeiras","Flamengo",
         "São Paulo","Bahia","Cruzeiro","Atlético-MG",
         "Athletico-PR","Vasco da Gama","internacional","Juventude",
         "Grêmio","Bragatino","Criciúma","Fluminense",
         "Fatal Model vitória","Corinthians","Cuiabá","Atlético-GO")

print(f"Tabela do Brasileirão: ", end="")
for posicao, tab in enumerate(times):
    print(f"{tab}", end=", "if posicao != 19 else ". ")
print("\n=====================")

print(f"Os 5 primeiros colocados são: ", end="")
for primeiros in range(0, 6):
    print(f"{times[primeiros]}", end=", " if primeiros != 5 else ". ")
print("\n=====================")

print(f"Os 4 ultimos colocados são: ", end="")
for ultimos in range(-4, 0):
    print(f"{times[ultimos]}", end=", "if ultimos != -1 else ". ")
print("\n======================")

print(f"A tabela em oredem alfabetica: ", end="")
for pos, time in enumerate(sorted(times)):
    print(f"{time}", end=", " if pos != 19 else ". ")
print("\n======================")

print(f"O Corinthians está atualmente na {times.index("Corinthians")+1}ª posição")