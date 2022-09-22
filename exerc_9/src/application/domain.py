import random
from typing import List
def lista_aleatória()->List[int]:
    lista_num = [random.randint(1,100)for x in range(10)]
    return lista_num

def busca_sequencial(lista_num:List[int],recebe_numero:int)->bool:
   
    if recebe_numero in lista_num:
        found = True
    else:
        found = False
    
    return found