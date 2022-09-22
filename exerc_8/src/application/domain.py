import random
from typing import List
def lista_aleatória()->List[int]:
    lista_num = [random.randint(1,100)for x in range(10)]
    lista_num.sort()
    return lista_num
    
def pesquisa_binaria(lista_num, numero):
    inicio = 0
    fim = len(lista_num)-1
    found = False
	
    while inicio<=fim and not found:
        meio_da_lista = (inicio + fim)//2
        if lista_num[meio_da_lista] == numero:
            found = True
        else:
            if numero < lista_num[meio_da_lista]:
                fim = meio_da_lista-1
            else:
                inicio = meio_da_lista+1	
    return found	
    	
        
