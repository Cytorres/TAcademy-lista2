from datetime import datetime, date
from typing import Tuple

def recebe_data()->Tuple[date, date] :
    str_data = input('Entre com a data inicial [dia/mes/ano]: ')
    data_inicial = datetime.strptime(str_data,'%d/%m/%Y').date()
    str_data = input('Entre com a data final [dia/mes/ano]: ')
    data_final = datetime.strptime(str_data,'%d/%m/%Y').date()
    
    return data_inicial, data_final

def mostra(data_inicial:datetime,data_final:datetime)->None:
    print(data_inicial,data_final)

