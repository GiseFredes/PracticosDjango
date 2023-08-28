"""6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad."""
class Persona:
    def __init__(self, nombre = "", edad = 0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    @property
    def get_nombre(self):
        return self.nombre
    @property
    def get_edad(self):
        return self.edad
    @property
    def get_dni(self):
        return self.dni
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre:
            self.__nombre = nuevo_nombre
    @edad.setter
    def edad(self, nuevo_edad):
        if nuevo_edad >=0:
            self.nombre = nuevo_edad
    @dni.setter
    def dni(self, nuevo_dni):
        if len(nuevo_dni)==8:
            self.nombre = nuevo_dni
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
try:
    p1 = Persona("Maxi", 13, "12345678")
    p1.mostrar()
    print("Es mayor de edad") if p1.es_mayor_de_edad() else print("Es menor de edad")
    
    print(f"Nombre {p1.nombre}\nEdad: {p1.edad}\nDNI: {p1.dni}")
    
    p1.nombre = "Cami"
    p1.edad = 12
    p1.dni = 14785236
    p1.mostrar()
except: 
    print("Picaro")