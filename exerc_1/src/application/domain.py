from typing import List


def abrir_arquivo()->List[str]:
    with open('src/application/menu.txt','r') as arquivo:
        menu = arquivo.readlines()

    return menu

print(abrir_arquivo())

def pegar_opcao_menu(menu:List[str],opcao:int)->None:
    while True:
        if opcao == 1:
            print(menu[0])
            break
        elif opcao == 2:
            print(menu[1])
            break
        elif opcao == 3:
            print(menu[2])
            break
        elif opcao == 4:
            print(menu[3])
            break
        elif opcao == 5:
            print(menu[4])
            break
        elif opcao == 6:
            break
        else:
            print('Opção inválida, tente novamente')
            continue
    
    
