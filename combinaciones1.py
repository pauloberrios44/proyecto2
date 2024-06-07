from functions import area_circulo, area_cuadrado, area_rectangulo

# Inicio de lógica

radio = input ('Ingresa el radio del círculo: ')
cara = input ('Ingresa la medida de una cara del cuadrado: ')
caraMenor = input ('Ingresa la cara menor del cuadrado: ')
caraMayor = input ('Ingresa la cara mayor del cuadrado: ')

# Calculando areas

print('================')
print('el área del círculo es: ' + str(area_circulo(radio)))
print('el area del cuadrado es: ' + str(area_cuadrado(cara)))
print('el área del rectangulo es: ' + str(area_rectangulo(caraMenor, caraMayor)))