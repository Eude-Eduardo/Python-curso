# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
user = str(input("Crie um nome de usuário: "))
print(f"""A senha deve conter:
- 8 caracteres
- Não pode ser igual ao nome de usuario
- Deve conter caracter especial '@#$%¨&*()~^/-+|'""")
print("__________")
password = str(input("Crie uma senha: "))
while password.upper() == user.upper() or len(password) <=7 or (not any(carac in "@#$%¨&*()~^/-+|" for carac in password)):
    if password.upper() == user.upper():
        password = str(input("Senha idêntica ao nome de usuário! Digite a senha novamente: "))
    elif len(password) <= 7:
        password = str(input("Menos de 8 caracteres! digite novamente: "))
    elif not any(carac in "@#$%¨&*()~^/-+|" for carac in password):
        password = str(input("Não contem caracteres especiais! "))

print(f"Nome: '{user}' e senha: '{password}' registrada com sucesso.")