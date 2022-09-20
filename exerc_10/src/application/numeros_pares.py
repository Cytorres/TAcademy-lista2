
from typing import List


def coloca_numero_lista(numeros:int,lista_de_numeros:List[int])-> List[int]: 
    lista_de_numeros.append(numeros)
    return lista_de_numeros

def sai_do_loop()->None:return input('Aperte [P] para parar')
    

def separa_numeros_pares(lista_de_numeros:List[int])->List[int]:
    somente_pares = []
    for numero in lista_de_numeros:
        if numero % 2 == 0:
            somente_pares.append(numero)            
    return somente_pares