numero = int(input('Digite el anho que desea consultar: '))

def Bisiesto(anho):
    if numero % 4 == 0:
        print('Anho ' + str(numero) + ' es bisiesto')
    else:
        print('Anho ' + str(numero) + ' NO es bisiesto')

Bisiesto(numero)