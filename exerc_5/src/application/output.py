from datetime import datetime

def mostra_dias(dias:int)->str:
    return print(f"Dias entre as datas {dias}")
    
def qtd_domingos(domingos:int,data_inicial:datetime,data_final:datetime)->str:
    return print (f"Entre a data {data_inicial} e {data_final}, terá {domingos} domingos.")