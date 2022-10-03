from src.application.input import opcao_menu
from src.application.domain import abrir_arquivo
from src.application.output import mostra_menu,mensagem

if __name__ == '__main__':
    menu = abrir_arquivo()
    opcao = menu
    FIM_OPCAO = 0
    while True:
        mensagem('Escolha a opção:')
        mostra_menu(menu)
        opcao = opcao_menu()
        if opcao == FIM_OPCAO:
            break
        el_menu = menu.get(opcao)
        if (el_menu is None):
            mensagem("Opção Invalida!")
        else:
            mensagem(menu[opcao])
