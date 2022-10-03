from typing import Dict

def abrir_arquivo()->Dict:
    menu = {}
    with open('src/application/menu.txt','r',encoding="utf-8") as arquivo:
        for elemento in arquivo:
            opcao_menu = elemento.replace("\n","").split(';')
            menu[opcao_menu[0]] = opcao_menu[1]
    return menu
