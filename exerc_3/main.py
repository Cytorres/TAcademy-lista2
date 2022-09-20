from src.application.input import recebe_valor
from src.application.numeros_primos import calcula_numeros_primos
from src.application.output import mensagem,mostra_lista

if __name__=='__main__':
    mensagem_de_inicio = mensagem('Digite um número para saber quantos números primos tem até esse valor.') 
    valor = recebe_valor()
    lista_de_primos = calcula_numeros_primos(valor)
    mostra_lista(lista_de_primos)