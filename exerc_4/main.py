from src.application.input import recebe_numero
from src.application.numeros_primos import numeros_primos
from src.application.output import mostra_lista

if __name__=='__main__':
    valor = recebe_numero()
    lista_de_numeros_primos = numeros_primos(valor)
    mostra_lista(lista_de_numeros_primos)