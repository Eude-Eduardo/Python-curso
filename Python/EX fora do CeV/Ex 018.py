arq = float(input("Qual o tamanho do arquivo em MB: "))
vel = int(input("Qual a velocidade da sua internete em Mbps: "))
tempo = arq*8/vel

print(f"O tempo para baixar {arq:.2f}MB é de {tempo // 60:.0f} minutos e {tempo % 60:.0f} segundos")