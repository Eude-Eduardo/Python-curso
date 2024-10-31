"""dados = {
    'Nome': "Eude",
    'Idade': 20,
    'sexo': "M"
    
}
filme = {
    "Título": "Star Wars",
    "Ano": 1997,
    "Diretor": "George Lucas"
}
# del(dados["sexo"])
print(dados.keys())
print(dados.values())
print(dados.items())
print(dados)"""
pessoas = {
    "Nome": "Eude",
    "Sexo": "M",
    "Idade": 20
}
del(pessoas["Sexo"])
pessoas["Peso"] = 83
for k, v in pessoas.items():
    print(f"{k} = {v}")
"""print(pessoas.items())
print(f"O {pessoas["Nome"]} tem {pessoas['Idade']} anos")"""