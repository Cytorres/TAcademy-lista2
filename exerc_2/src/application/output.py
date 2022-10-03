from typing import Dict

def mostra_menu(menu:Dict)->None:

    for key, value in menu.items():
        print(f"{key} : {value}")

def mensagem(msg):
    print(msg)
