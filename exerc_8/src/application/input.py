def recebe_numero():
    while True:
        try:
            numero = int(input('Digite um número de 0 a 100: '))
        except:
            print("ERRO... Digite um número inteiro de 0 a 100.")
            continue
        if (numero < 0 or numero >100):
            print("ERRO... Digite um número inteiro entre 0 e 100.")
            continue
        if (numero >= 0 or numero <= 100):
            break
    return numero