minha_string = "xx_xxxxx_0001_ABCDE_TESTE_INTRODUCAO_VIDEO"
partes = minha_string.split("_")
ultimo_elemento = partes.pop()
print(f"A última parte é: {ultimo_elemento}")
