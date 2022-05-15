import time

def main():
    
    hora = int(time.strftime('%H'))
    minutos = int(time.strftime('%M'))

    if hora <  19:
        hora = 18 - hora
        minutos = 60 - minutos
        print(f"Faltan {hora} horas y {minutos} minutos para salir")
    else:
        print("Ya esa hora de salir")


if __name__ == '__main__':
    main()    