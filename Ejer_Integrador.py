#Ejercicios integradores para revisar en la clase 7
#***************************************************
import funciones
#1. Escribir una función que calcule el máximo común divisor entre dos números.
"""print("El siguiente código encuentra el MCD entre dos números enteros.")
num1=int(input("Ingrese el primer valor mayor a 0: "))
num2=int(input("Ingrese el segundo valor mayor a 0: "))
if(num1>0 and num2>0):
    funciones.calcularMCD(num1, num2)
else:
    print("El o los valores ingresador son incorrectos")
print("FIN DEL PROGRAMA")
#Funciona
####################################################################################"""
#2. Escribir una función que calcule el mínimo común múltiplo entre dos números
"""print("El siguiente código encuentra el MCM entre dos números enteros.")
num1 = int(input('Ingrese el primer valor mayor que 0: '))
num2 = int(input('ingrese el segundo valor mayor que 0: '))
if num1 > num2:
    menor =num2
else:
    menor = num1
    num1 = num2
funciones.calcularMCM(menor, num1)
print("FIN DEL PROGRAMA")
#Funciona
####################################################################################"""
#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
"""
cadena=input('Ingrese una cadena de texto:')
funciones.dic(cadena)
print("FIN DEL PROGRAMA")
#Funciona
#####################################################################################"""

#4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
#palabra más repetida y su frecuencia."""

"""print("Este programa recibe una cadena de texto y luego clasifica la cantidad de veces que aparece cada palabra por último muestra la de mayor fecuencia")
cadenita=input("Ingrese una cadena de texto: ")
print("")
funciones.frecuencia(funciones.dic(cadenita))
print("FIN DEL PROGRAMA")"""
#Funciona
#####################################################################################"""

"""5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
ejercicio tanto de manera iterativa como recursiva."""


"""print("En este programa podes ingresar una cantidad de números hasta que ingreses una letra")
lista_enteros = []
funciones.get_int(lista_enteros)"""
#Funciona
######################################################################################
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

"""7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos."""
"""8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta."""