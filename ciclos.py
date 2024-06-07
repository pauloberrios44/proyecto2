#                    0       1        2
arrayInstitutos = ['AIEP', 'DUOC', 'CIISA']
valorIndice = 4

try:
    print (arrayInstitutos[valorIndice])
except:
    print('Se produjo un error')








frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# Bucle for con índices
colores = ["rojo", "verde", "azul"]
for i in range(len(colores)):
    print(i, colores[i])

# # Ejemplo de bucle for
# frutas = ["manzana", "banana", "naranja"]
# for fruta in frutas:
#     print(fruta)

# # Bucle for con índices
# colores = ["rojo", "verde", "azul"]
# for i in range(len(colores)):
#     print(i, colores[i])

# # Bucle for anidado
# numeros = [[1, 2], [3, 4], [5, 6]]
# for fila in numeros:
#     for num in fila:
#         print(num)

# # Ejemplo de bucle while
# numero = 1
# while numero <= 5:
#     print(numero)
#     numero += 1

# # Bucle while con condición de salida
# respuesta = ""
# while respuesta != "salir":
#     respuesta = input("Ingresa 'salir' para terminar: ")

# Bucle while anidado
fila = 1
while fila <= 3:
    columna = 1
    while columna <= 3:
        print(fila, columna)
        columna += 1
    fila += 1