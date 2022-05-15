class Vehiculo():
    color = "rojo"
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 1200

nuevoCoche = Coche()

print("El color de coche es " + nuevoCoche.color)
print("Numero de ruedas del coche " + str(nuevoCoche.ruedas))
print("Numero de puertas del coche " + str(nuevoCoche.puertas))
print("La velocidad del coche es " + str(nuevoCoche.velocidad))
print("La cilindrada del coche es " + str(nuevoCoche.cilindrada))



