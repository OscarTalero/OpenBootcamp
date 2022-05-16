from functools import reduce

def main():

    numeros = [1,2,3,4,5,6,7,9]
    print(f'Lista de numeros: {numeros}')

    resultado = filter(lambda x : x % 2, numeros)
    impares = list(resultado)
    print(f'Los numeros impares son: {impares}')

    print(f'La suma de los numeros impares es: {reduce(lambda a,b : a + b, impares)}')


if __name__ == '__main__':
    main()

