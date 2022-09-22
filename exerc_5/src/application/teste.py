from datetime import datetime

data_inicial = input('Entre com a data inicial [dia/mes/ano]: ')
data_inicial = datetime.strptime(data_inicial,'%d/%m/%Y').date()
data_final = input('Entre com a data final [dia/mes/ano]: ')
data_final = datetime.strptime(data_final,'%d/%m/%Y').date()
data1 = data_inicial.toordinal() #Convertendo em dias
data2 = data_final.toordinal()
dias = data2 - data1

print(data1)
print(data2)