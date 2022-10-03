from src.application.input import abrir_arquivo,opcao_menu
from src.application.output import mostra_menu,mensagem

if __name__ == '__main__':
    menu = abrir_arquivo()
    fim_menu = len(menu)+1
    while True:
        print('Escolha a opção:')
        mostra_menu(menu)
        opcao = opcao_menu()
        if opcao == fim_menu:
            break
        if opcao not in range(1,fim_menu):
            mensagem('Opção inválida\n')
        else:
            mensagem(menu[opcao-1])
