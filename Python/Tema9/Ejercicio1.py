def main():

    paises = input("Ingrese los paises separados por coma: ")
    paisesOrdenados = sorted(set(paises.split(",")))

    for pais in paisesOrdenados:

        print(f'{pais}, ', end = '')

    print('')

if __name__ == '__main__':
    main()

