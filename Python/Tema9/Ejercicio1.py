def main():

    paises = input("Ingrese los paises separados por coma: ")
    listaPaises = set(paises.split(","))
    paisesOrdenados = sorted(listaPaises)

    for pais in paisesOrdenados:

        print(f'{pais}, ', end = '')

    print('')
    
if __name__ == '__main__':
    main()

