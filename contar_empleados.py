employees = ['andres', 'cynthia', 'cynthia', 'cynthia', 'guillermo', 'andres']

for nombreBuscado in employees:
    contador = 0
    for nombre in employees:
        if nombreBuscado == nombre:
            contador = contador + 1
    print ('El empleado ' + nombreBuscado + ' se encuentra registrado ' + str(contador) + ' veces')