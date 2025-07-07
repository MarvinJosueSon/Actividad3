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
                    break
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

def IngresarMascota():
    try:
        existe=False
        cuiAux=int(input("Ingrese el cui del cliente: "))
        for cl in ClientesList:
            if cl.cui == cuiAux:
                existe=True
                dueñoAux=cl
        if existe:
            print("1. Gato")
            print("2. Perro")
            print("3. Otro")
            opcionAux=input("Seleccione el tipo de animal a ingresar: ")
            if opcionAux == "1" or opcionAux == "2" or opcionAux == "3":
                nombreAux=input("Ingrese el nombre de la mascota: ")
                edadAux=int(input("Ingrese la edad de la mascota (en meses): "))
                pesoAux=int(input("Ingrese el peso de la mascota (en libras): "))
                if opcionAux == "1":
                    especieAux="Gato"
                    colorAux=input("Ingrese el color del gato: ")
                    gatoAux=Gato(nombreAux,edadAux,pesoAux,especieAux,dueñoAux,colorAux)
                    dueñoAux.AgregarMascota(gatoAux)
                    print("Mascota ingresada con exito")
                elif opcionAux == "2":
                    especieAux="Perro"
                    razaAux=input("Ingrese la raza del perro: ")
                    perroAux=Perro(nombreAux,edadAux,pesoAux,especieAux,dueñoAux,razaAux)
                    dueñoAux.AgregarMascota(perroAux)
                    print("Mascota ingresada con exito")
                elif opcionAux == "3":
                    especieAux="Otro"
                    tipoAux=input("Ingrese la tipo de mascota (reptil, ave, pez, etc): ")
                    otroAux=Otro(nombreAux,edadAux,pesoAux,especieAux,dueñoAux,tipoAux)
                    dueñoAux.AgregarMascota(otroAux)
                    print("Mascota ingresada con exito")

            else:
                print("Opcion no existe")
        else:
            print("Cliente no existe")
    except ValueError:
        print("ERROR: EDAD Y PESO DEBEN IR EN NUMEROS ENTEROS")
def IngresarCitaMedica():
    try:
        existe=False
        cuiAux=int(input("Ingrese el  cui del cliente: "))

        for cl in ClientesList:
            if cl.cui == cuiAux:
                existe=True
                dueñoAux=cl
        if existe:
            if len(dueñoAux.mascotas)>0:
                i=1
                print("Mascotas registradas")
                for mascota in dueñoAux.mascotas:
                    print(f"{i}. {mascota.nombre} ")
                    i=i+1
                opcionAux=int(input("Seleccione el numero de mascota: "))
                if opcionAux >=1 and opcionAux<=len(dueñoAux.mascotas):
                    mascotaAux=dueñoAux.mascotas[opcionAux-1]
                    descripcionAux=input("Ingrese la descripcion de la cita medica: ")
                    fechaAux=input("Ingrese la fecha de la cita medica: ")
                    citaAux=CitaMedica(mascotaAux,descripcionAux,fechaAux)
                    CitasList.append(citaAux)
                else:
                    print("Mascota no encontrada")
            else:
                print("El cliente aun no tiene mascotas registradas")
        else:
            print("Cliente no existe")
    except ValueError:
        print("ERROR")
def verClientes():
    if  len(ClientesList)>0:
        for cl in ClientesList:
            cl.Mostrar()
            for mascota in cl.mascotas:
                mascota.Mostrar()
            print("")
while True:
    print("==MENU==")
    print("1. Ingresar Cliente")
    print("2. Ingresar Mascota")
    print("3. Ingresar Cita Medica")
    print("4. Ver clientes")
    print("5. Ver Citas programadas")
    print("6. Salir")
    opcion=input("Ingrese una opcion: ")
    match opcion:
        case "1":
            IngresoCliente()
        case "2":
            IngresarMascota()
        case "3":
            IngresarCitaMedica()
        case "4":
            verClientes()
