def calcula_numeros_primos(valor):
    lista_primos = []
    for numero in range(2,valor+1):
        if numero > 1:
            for valor in range(2,numero):
                if(numero % valor == 0):
                    break
            else:
                lista_primos.append(numero)
    return lista_primos


        