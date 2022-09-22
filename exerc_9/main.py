from src.application.input import recebe_numero
from src.application.domain import lista_aleatória,busca_sequencial
from src.application.output import resultado_da_pesquisa

if __name__=="__main__":
    numero = recebe_numero()
    lista_num = lista_aleatória()
    found = busca_sequencial(lista_num,numero)
    resultado_da_pesquisa(lista_num,numero,found)