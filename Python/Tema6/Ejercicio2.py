class Alumno:
    def inicializar(self, nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def aprobado(self):
        if self.nota < 5:
            print(f"El alumno {self.nombre}, con nota de {self.nota} fue: REPROBADO")
        else:
            print(f"El alumno {self.nombre}, con nota de {self.nota} fue: APROBADO")
    
alumno = Alumno()
alumno.inicializar("Jhon",7)
alumno.imprimir()
alumno.aprobado()
