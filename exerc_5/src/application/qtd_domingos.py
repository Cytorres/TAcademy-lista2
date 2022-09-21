def calcula_qtd_dias(data_inicial,data_final):
    data1 = data_inicial.toordinal() #Convertendo em dias
    data2 = data_final.toordinal()
    dias = data2 - data1
    return dias

def calcula_quantidade_domingos(dias):
    domingos = round(dias / 7)
    return domingos