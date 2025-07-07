class Mascota:
    def __init__(self,nombre,edad,peso,especie):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.especie = especie
class Gato(Mascota):
    def __init__(self,nombre,edad,peso,especie,color):
        super().__init__(nombre, edad, peso, especie)
        self.color= color
