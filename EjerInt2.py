import funciones
#2. Escribir una función que calcule el mínimo común múltiplo entre dos números
print("El siguiente código encuentra el MCM entre dos números enteros.")
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