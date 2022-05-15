import calculadora as calc

def main():
    a = 6
    b = 3
    suma = calc.sumar(a,b)
    resta = calc.restar(a,b)
    multiplica = calc.multiplicar(a,b)
    divide = calc.dividir(a,b)
    print(f"La suma: {a} + {b} = {suma}")
    print(f"La resta: {a} - {b} = {resta}")
    print(f"La multiplicacion: {a} x {b} = {multiplica}")
    print(f"La division de {a} / {b} = {divide}")


if __name__ == '__main__':
    main()