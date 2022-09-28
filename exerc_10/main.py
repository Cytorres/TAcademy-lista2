from src.application.output import mostra_mensagem
from src.application.input import recebe_numero
from src.application.numeros_pares import sai_do_loop,separa_numeros_pares

if __name__=='__main__':
    lista_de_numeros = [] 
    while True:
        try:
            numero = recebe_numero()
        except:
            print('Digite um número.')
            continue

        lista_de_numeros.append(numero)

        parar_sistema = sai_do_loop().upper()
       
        if parar_sistema != "P":
            print('Comando invalido')
        else:
            break

    print(lista_de_numeros)
    somente_pares = separa_numeros_pares(lista_de_numeros)
    mostra_mensagem(f'Numeros pares {somente_pares}')


