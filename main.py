ClientesList=[]
CitasList=[]
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
def IngresoCliente():
    while True:
        try:
            existe=False
            nombreAux=input("Ingrese nombre: ")
            cuiAux=int(input("Ingrese cui: "))
            for cl in ClientesList:
                if cl.cui == cuiAux:
                    existe=True
            telefonoAux=int(input("Ingrese telefono: "))
            ClienteAux=Cliente(nombreAux,cuiAux,telefonoAux)
            if not existe:
                ClientesList.append(ClienteAux)
                print("Cliente creado con exito")
                break
            else:
                print("Cliente ya existe")
                opcionAux = input("Regresar al menu principal? s/n: ").lower()
                if opcionAux == "s":
                    break
        except ValueError:
            print("ERROR: CUI Y TElEFONO deben ser numericos")
            opcionAux= input("Regresar al menu principal? s/n: ").lower()
            if opcionAux == "s":
                break


while True:
    print("==MENU==")
    print("1. Ingresar Cliente")
    print("2. Ingresar Mascota")
    print("3. Ingresar Cita Medica")
    print("4. Ver clientes")
    print("5. Ver Citas programadas")
    opcion=input("Ingrese una opcion: ")
    match opcion:
        case "1":
            IngresoCliente()
