from src.application.input import recebe_numero
from src.application.domain import lista_aleatória,pesquisa_binaria
from src.application.output import resultado_da_pesquisa
if __name__ == "__main__":
    numero = recebe_numero()
    lista = lista_aleatória()
    found = pesquisa_binaria(lista,numero)
    resultado_da_pesquisa(lista,numero,found)
