"""6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad."""
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad no puede ser negativa.")

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        if len(dni) == 9:
            self.dni = dni
        else:
            print("El DNI debe tener 9 caracteres.")

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)

    def es_mayor_de_edad(self):
        return self.edad >= 18


# Ejemplo 
persona1 = Persona()
persona1.set_nombre("Maximiliano")
persona1.set_edad(13)
persona1.set_dni("50525869")

persona1.mostrar()
if persona1.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")
    

try:
    p1 = Persona("Anibal", 39, "12345678")
    p1.mostrar()
    print("Es mayor de edad") if p1.es_mayor_de_edad() else print("Es menor de edad")
    
    print(f"Nombre {p1.nombre}\nEdad: {p1.edad}\nDNI: {p1.dni}")
    
    p1.nombre = "Cami"
    p1.edad = 12
    p1.dni = 14785236
    p1.mostrar()
except: 
    print("Picaro")