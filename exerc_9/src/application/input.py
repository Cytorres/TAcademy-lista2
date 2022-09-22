def recebe_numero()->int:
    while True:
        try:
            recebe_numero = int(input('Digite um número de 1 a 100: '))

        except:
            print('ERRO... Digite um número inteiro de 1 a 100.')
            continue

        if (recebe_numero < 1 or recebe_numero > 100):
            print("ERRO... Digite um número inteiro entre 1 e 100.")
            continue
        if (recebe_numero >= 1 or recebe_numero <= 100):
            break
    
    return recebe_numero