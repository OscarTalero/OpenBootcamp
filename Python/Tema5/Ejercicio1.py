base = int(input("Ingrese la base del triangulo: "))
altura = int(input("ingrese la altura del triangulo: "))

AreaTriangulo = lambda base,altura : print(round((float(base) * float(altura))/2,2))
AreaTriangulo(base,altura)

radio = int(input("ingrese el radio del circulo: "))

AreaCirculo = lambda radio : print(round(3.14 * float(radio**2),2))

AreaCirculo(radio)