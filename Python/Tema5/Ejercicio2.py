numero = int(input('Ingrese un numero: '))

def Primo(numero):
    if numero > 1:
        for i in range(2,numero):
            if numero % i == 0:
                print('Numero ' + str(numero) + ' no es primo')
                break
        else:
            print('Numero ' + str(numero) + ' es primo')

Primo(numero)