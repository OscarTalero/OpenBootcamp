import pickle


class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self) -> str:
        return f'Vehiculo de color {self.color}, con {self.ruedas} ruedas'
    
coche = Vehiculo("rojo", 4)

f = open('datos.bin', 'wb')
pickle.dump(coche, f)
f.close

f = open('datos.bin', 'rb')
coche1 = pickle.load(f)
f.close()

print(coche1)