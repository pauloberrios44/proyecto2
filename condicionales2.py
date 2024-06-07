

# array1 = [1,2,3,4,5,6]
# array2 = [4,5,8]

# print('Iniciando el recorrido')
# for item in array1:
#     encontrado = False
#     for item2 in array2:
#         if item == item2:
#             print('El elemento ' + str(item) + ' ha sido encontrado')
#             encontrado = True
#             break
#     if not encontrado:
#         print ('El elemento ' + str(item) + ' no fue encontrado en el array2')


paisesConNuevaComision = ['US', 'CA']
nuevaComision = 0.245
paisesEmpleados = ['CL', 'PE', 'US']

# Buscando paises de empleados entre los paises autorizados con nueva comision

for paisConNuevaComision in paisesConNuevaComision:
    encontrado = False
    for paisEmpleado in paisesEmpleados:
        if paisEmpleado == paisConNuevaComision:
            print ('El pais ' + paisEmpleado + ' tiene pago por nueva comisión')
            encontrado = True
            break
    if not encontrado:
        print ('El pais ' + paisConNuevaComision + ' no fue encontrado entre los paises de los empleados contratados')