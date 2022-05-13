numero_inicial = int(input("Ingresa el numero inicial: "))
numero_final = int(input("Ingresa el numero final: "))
numeros_impares = []

while numero_inicial > numero_final:
    numero_inicial = int(input("El numero inicial debe ser menor. Ingresa otro numero12"))

while numero_inicial < numero_final:
    if (numero_inicial % 2) == 1:
        numeros_impares.append(numero_inicial)
    numero_inicial +=1

print(numeros_impares)
