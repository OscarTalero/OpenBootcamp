class Vehiculo():

    def __init__(self,color,ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return f"Color {self.color}, {self.ruedas} ruedas, {self.puertas} puertas"

class Coche(Vehiculo):

    def __init__(self,color,ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color {self.color}, {self.ruedas} ruedas, {self.puertas} puertas, {self.velocidad} k/h, {self.cilindrada} CC"

coche = Coche("rojo",4,2,200,1600)
print(coche)




