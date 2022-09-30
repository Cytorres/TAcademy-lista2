from datetime import date, timedelta


def calcula_qtd_dias(data_inicial:date, data_final:date)->int:
    data1 = data_inicial.toordinal() #Convertendo em dias
    data2 = data_final.toordinal()
    dias = data2 - data1
    return dias

def calcula_quantidade_domingos2(data_inicial: date, data_final: date) -> int:
    dia_semana = data_inicial.weekday()
    dias_somar = 6 - dia_semana

    nova_data_inicial = data_inicial + timedelta(days=dias_somar)
    numero_domingos = 0
    while (nova_data_inicial <= data_final):
        nova_data_inicial += timedelta(days=7)
        numero_domingos += 1

    return numero_domingos


def calcula_quantidade_domingos(data_inicial: date, data_final: date) -> int:
    dia_semana = data_inicial.weekday()
    dias_somar = 6 - dia_semana

    nova_data_inicial = data_inicial + timedelta(days=dias_somar)
    numero_domingos = 0
    if (nova_data_inicial <= data_final):
        numero_domingos += 1

    dif_dias = calcula_qtd_dias(nova_data_inicial, data_final)
    if (dif_dias > 0):
        numero_domingos += dif_dias // 7
        
    return numero_domingos
