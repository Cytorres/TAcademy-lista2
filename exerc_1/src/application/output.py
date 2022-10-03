from typing import List

def mostra_menu(menu:List[str])->None:
    for elemento in menu:
        print(elemento, end ='')
    print('\n6;FIM')

def mensagem(msg:str) -> None:
    print(msg)
