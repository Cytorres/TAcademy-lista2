from datetime import date


def calcula_qtd_dias(data_inicial:date ,data_final:date)->int:
    data1 = data_inicial.toordinal() #Convertendo em dias
    data2 = data_final.toordinal()
    dias = data2 - data1
    return dias

def calcula_quantidade_domingos(dias:int)->int:
    domingos = (dias // 7)
    return domingos