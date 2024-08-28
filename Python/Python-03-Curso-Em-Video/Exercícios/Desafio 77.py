palavras = ("tanto", "externa", "continuo", "codorna", "surgiu", "sortida", "ditoso", "cumprido", "confiante", "brilhoso", "vetado", "estabelece")

for palavra in palavras:
    print(f"\nVogais da palavra {palavra}: ", end="")
    
    for letras in palavra:
        
        if letras.upper() in "AEIOU":
            print(f"{letras}", end=" ")
