from src.application.input import recebe_data
from src.application.qtd_domingos import calcula_qtd_dias,calcula_quantidade_domingos
from src.application.output import mostra_dias,qtd_domingos

if __name__ =='__main__':
    data_inicial,data_final = recebe_data()
    dias = calcula_qtd_dias(data_inicial,data_final)
    domingos = calcula_quantidade_domingos(dias)
    qtd_dias = mostra_dias(dias)
    mostra_domingos = qtd_domingos(domingos,data_inicial,data_final)



