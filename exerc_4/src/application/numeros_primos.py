from typing import List


def numeros_primos(valor:int)->List[int]:
    lista_de_numeros_primos = [x for x in range(2, valor) if all(x % y != 0 for y in range(2, x))]
    return lista_de_numeros_primos