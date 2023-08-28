import funciones
#4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
#palabra más repetida y su frecuencia."""

print("Este programa recibe una cadena de texto y luego clasifica la cantidad de veces que aparece cada palabra por último muestra la de mayor fecuencia")
cadenita=input("Ingrese una cadena de texto: ")
print("")
funciones.frecuencia(funciones.dic(cadenita))
print("FIN DEL PROGRAMA")
#Funciona