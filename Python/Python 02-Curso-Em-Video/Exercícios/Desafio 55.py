ps = []
for peso in range (1, 6):
    ps.append(float(input("Digite opeso? (Kg) ")))

print(
    f"O maior peso foi {max(ps)}Kg\n"
    f"O menor peso foi {min(ps)}Kg"
)
