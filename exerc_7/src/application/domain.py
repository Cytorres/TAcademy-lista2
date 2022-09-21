import random
from typing import List
def lista_aleatória()->List[int]:
    lista_num = [random.randint(1,100)for x in range(10)]
    return lista_num

def busca_sequencial(lista_num:List[int],recebe_numero:int)->bool:
    posicao = 0
    found = False
    while posicao < len(lista_num) and not found:
        if lista_num[posicao] == recebe_numero:
            found = True
        else: 
            posicao +=1
    
    return found