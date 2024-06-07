# SECCION DE DECLARACION DE FUNCIONES

def area_circulo(radio):
    return 3.14 * float(radio) ** 2

def area_cuadrado(cara):
    return float(cara) * float(cara)

def area_rectangulo(caraMenor, caraMayor):
    return float(caraMenor) * float(caraMayor)

def contar_nombres(arrayNombres):
    for nombreBuscado in arrayNombres:
        contador = 0
        for nombre in arrayNombres:
            if nombreBuscado == nombre:
                contador = contador + 1
        print ('El empleado ' + nombreBuscado + ' se encuentra registrado ' + str(contador) + ' veces')