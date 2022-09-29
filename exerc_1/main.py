from src.application.input import opcao_menu
from src.application.domain import abrir_arquivo
from src.application.output import mostra_menu

if __name__ == '__main__':
    menu = abrir_arquivo()
    mostra_menu(menu)
    opcao = opcao_menu()