#1. Escribir una función que calcule el máximo común divisor entre dos números.
"""Todas las funciones estan en la pestaña funciones"""
import funciones
print("El siguiente código encuentra el MCD entre dos números enteros.")
num1=int(input("Ingrese el primer valor mayor a 0: "))
num2=int(input("Ingrese el segundo valor mayor a 0: "))
if(num1>0 and num2>0):
    funciones.calcularMCD(num1, num2)
else:
    print("El o los valores ingresador son incorrectos")
print("FIN DEL PROGRAMA")
#Funciona
"""Este programa lo pense en un primer momento para llamar a la funcion de la biblioteca math. Pero desconfie en que fuera tan sencillo y por eso 
cree una funcion que la calculara manualmente."""