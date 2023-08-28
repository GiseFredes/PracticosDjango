def calcularMCD(num1,num2):
    maximo=1
    divisor=1
    while num1>divisor:
        if num1%divisor==0 and num2%divisor==0:
            maximo=divisor
        divisor=divisor+1
    print("El MCM es : ", maximo)

def calcularMCM(menor, num1):
    condicion=1
    while condicion!=0:
        mult1=num1*condicion
        condicion=condicion+1
        mult2=0
        condicion2=1
        while mult2<mult1:
            mult2=menor*condicion2
            condicion2=condicion2+1
            if(mult1==mult2):
                print('El minimo comun multiplo es: ', mult1)
                condicion=0
def dic(cadena):
    lista1=cadena.split()
    #print(type(lista1))
    diccionario=dict.fromkeys(lista1)

    #print(diccionario)
    for iterador in lista1:
        diccionario[iterador]=lista1.count(iterador)
    print("Palabra   Frecuencia")
    print("---------------------")
    
    for key, value in sorted(diccionario.items(), key=lambda x: x[1]):
        print(f"{key}: {value}")
    print("*********************")
    print("Fin del conteo de palabras") 
    n=input("Presione cualquier tecla para continuar!!!")
    print("")
    return diccionario   

def frecuencia(dicci):
    print("Esta parte determina cual es la palabra que más se repite y su frecuencia")
    print("")
    d=input("Presione cualquier tecla para ver la palabra ganadora!!!")
    mayor=1
    posicion=0
    for iterador in dicci:
        if dicci[iterador] > mayor:
            mayor=dicci[iterador]
            posicion=iterador
    tupla=(posicion,mayor)
    print("----------------------------")
    print("Palabra Frecuencia")
    print(tupla)
    
def get_int(lista_enteros):
    try:
        num=int(input("Ingrese un número, -1 para terminar: "))
        lista_enteros.append(num)
        while num!=-1:
           num=int(input("Ingrese un número, -1 para terminar: ")) 
           lista_enteros.append(num)
        lista_enteros.pop() #Borro el ultimo elemento que es el menos 1 y no me interesa conservarlo
        return lista_enteros
    except:
        print("Debes ingresar un valor númerico")
        get_int(lista_enteros) #Aca para no terminar la vuelvo a llamar hasta que el ususario decide terminar de  ingresar números
#Me salio bien a la primera!!!!
#Diferencia que hay entre las soluciones propuestas y lo mio. No guardan todos los valores ingresados. 
#Yo los guardo en una lista, solo porque interprete que sería más util tenes los valores en un futuro problema
