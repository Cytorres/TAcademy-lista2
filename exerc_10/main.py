from src.application.output import mostra_mensagem
from src.application.input import recebe_numero
from src.application.numeros_pares import coloca_numero_lista,sai_do_loop,separa_numeros_pares

if __name__=='__main__':
    lista_de_numeros = [] 
    while True:
        try:
            armazena_numeros = recebe_numero()
        except:
            print('Digite um número.')
            continue
        lista_de_numeros = coloca_numero_lista(armazena_numeros,lista_de_numeros)

        parar_sistema = sai_do_loop().upper()
        
        if parar_sistema != "P":
            print('Comando invalido')

        if parar_sistema == "P": 
            print(lista_de_numeros)
            somente_pares = separa_numeros_pares(lista_de_numeros)
            mostra_mensagem(f'Numeros pares {somente_pares}')
            break
        else:
            continue    

