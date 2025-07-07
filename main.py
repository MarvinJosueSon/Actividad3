class Mascota:
    def __init__(self,nombre,edad,peso,especie,dueño):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.especie = especie
        self.dueño=dueño
    def Mostrar(self):
        print(f"Nombre: {self.nombre}; edad: {self.edad}; peso: {self.peso}; especie: {self.especie}")
        print("Dueño:")
        self.dueño.Mostrar()


class Gato(Mascota):
    def __init__(self,nombre,edad,peso,especie,dueño,color):
        super().__init__(nombre, edad, peso, especie,dueño)
        self.color= color
    def Mostrar(self):
        super().Mostrar()
        print(f"Color: {self.color}")
class Perro(Mascota):
    def __init__(self,nombre,edad,peso,especie,dueño,raza):
        super().__init__(nombre,edad,peso,especie,dueño)
        self.raza = raza
    def Mostrar(self):
        super().Mostrar()
        print(f"Raza: {self.raza}")
class Otro(Mascota):
    def __init__(self,nombre,edad,peso,especie,dueño,tipo):
        super().__init__(nombre,edad,peso,especie,dueño)
        self.tipo=tipo
    def Mostrar(self):
        super().Mostrar()
        print(f"Tipo: {self.tipo}")
class Cliente:
    def __init__(self,nombre,cui,telefono):
        self.nombre = nombre
        self.cui = cui
        self.telefono = telefono
        self.mascotas = []

    def AgregarMascota(self,mascota):
        self.mascotas.append(mascota)
    def Mostrar(self):
        print(f"Nombre: {self.nombre}; cui: {self.cui}; telefono: {self.telefono}")

class CitaMedica:
    def __init__(self,mascota,descripcion,fecha):
        self.mascota = mascota
        self.descripcion = descripcion
        self.fecha = fecha
    def Mostrar(self):
        print(f"Descripcion: {self.descripcion}")
        self.mascota.Mostrar()

