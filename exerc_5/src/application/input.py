from datetime import datetime
def recebe_data()->str:
    data_inicial = input('Entre com a data inicial [dia/mes/ano]: ')
    data_inicial = datetime.strptime(data_inicial,'%d/%m/%Y').date()
    data_final = input('Entre com a data final [dia/mes/ano]: ')
    data_final = datetime.strptime(data_final,'%d/%m/%Y').date()
    return data_inicial,data_final

def mostra(data_inicial:int,data_final:int)->None:
    print(data_inicial,data_final)

