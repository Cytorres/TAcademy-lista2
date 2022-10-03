from typing import List

def abrir_arquivo()->List[str]:
    with open('src/application/menu.txt','r') as arquivo:
        menu = arquivo.readlines()
    return menu

def opcao_menu()->int:
    return int(input('\n_:'))
    