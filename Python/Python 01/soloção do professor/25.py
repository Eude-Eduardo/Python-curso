nome = str(input('Qual seu nome completo?')).strip()
print(f'Seu nome tem silva? {nome.lower().find('silva') != -1}')

print('Seu nome tem silva? {}'.format("silva" in nome.lower()))