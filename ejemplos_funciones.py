def calcular_area_rectangulo(caraMenor, caraMayor):
    areaRectangulo = caraMenor * caraMayor
    return areaRectangulo


print ('Calculo del área de un cuadrado')
caraMenor = input('Ingrese la cara menor')
caraMayor = input('Ingrese la cara mayor')
area = calcular_area_rectangulo(float(caraMenor), float(caraMayor))

print (f'El area del rectangulo es de {area}')
