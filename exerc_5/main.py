from src.application.input import recebe_data
from src.application.qtd_domingos import calcula_qtd_dias,calcula_quantidade_domingos
from src.application.output import mostra_mensagem

if __name__ =='__main__':
    data_inicial, data_final = recebe_data()
    dias = calcula_qtd_dias(data_inicial, data_final)
    domingos = calcula_quantidade_domingos(dias)
    mostra_mensagem(f"Dias entre as datas {dias}")
    mostra_mensagem(f"Entre a data {data_inicial} e {data_final}, terá {domingos} domingos.")
    


