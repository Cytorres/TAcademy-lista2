# lista_de_numeros_primos = [x for x in range(2, valor) if all(x % y != 0 for y in range(2, x))]
valor = 10
lista_primos=[]

if all(x % y != 0 for y in range(2, x):
    for x in range(2, valor):
        lista_primos.append(x)
print(lista_primos)