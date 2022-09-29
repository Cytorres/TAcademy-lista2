def abrir_arquivo():
    with open('src/application/menu.txt','r') as arquivo:
        menu = arquivo.readlines()

    return menu

print(abrir_arquivo())