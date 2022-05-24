meta_estado = {'A':'0', 'B':'0', 'C':'0'}
ubicacion_objetivo = input("Ingrese la ubicación del objetivo: ")

def ubicacion_objetivoA():   
    costo = 0  # Inicialización de costo
    # Ingeso de estados de los objetivos
    estado_objetivo1 = input("Ingrese el estado de " + ubicacion_objetivo + ": ")  
    estado_objetivo2 = input("Ingrese el estado de B: ")  
    estado_objetivo3 = input("Ingrese el estado de C: ")

    # Imprimir estado de la meta
    print('Meta deseada: ' + str(meta_estado) + ' deben ser eliminados')
    
    print("\nEl objetivo se coloca en el campo A") 

    # Caso 1: El objetivo está en el campo A
    if estado_objetivo1 == '1':
        print("En el campo A está el Objetivo no eliminado")
        # Eliminar el objetivo del campo A
        meta_estado['A'] = '0' # Cambiar el estado del objetivo en la meta a 0
        # Costo actual
        costo += 1
        # Imprimir costo actual y eliminación del objetivo en el campo A
        print("Eliminando Objetivo en el campo A")
        print("Costo actual: " + str(costo))

        # Caso 2: El objetivo está en el campo B
        if estado_objetivo2 == '1': # Estado de la ubicacion B
            print("\nEn el campo B está el Objetivo no eliminado")
            # Proyectil se dirige al campo B
            print("Dirigiendose a la ubicación B")
            costo += 1
            print("Costo actual: " + str(costo))
            # Eliminar el objetivo del campo B
            meta_estado['B'] = '0' # Convertir el estado del objetivo en 0
            costo += 1 # Costo creciente
            # Imprimir costo actual y eliminación del objetivo en el campo B
            print("Eliminando Objetivo en el campo B")
            print("Costo actual: " + str(costo)) 
        else: 
            # Caso contrario, el Objetivo está eliminado
            print("\nEn el campo B está el Objetivo eliminado")
            print("No se realizó ninguna acción")
            print("Costo actual: " + str(costo))

        # Caso 3: El objetivo está en el campo C
        if estado_objetivo3 == '1':
            print("\nEn la ubicación C está el Objetivo no eliminado")
            # Proyectil se dirige al campo C
            print("Dirigiendose al campo C")
            costo += 1
            print("Costo actual: " + str(costo))
            # Eliminar el objetivo del campo C
            meta_estado['C'] = '0' # Cambiar estado del objetivo en el campo C a 0
            costo += 1 # Costo creciente
            # Imprimir costo actual y eliminación del objetivo en el campo C
            print("Eliminando Objetivo del campo C")
            print("Costo actual: " + str(costo))
        else:
            # Caso contrario, el Objetivo está eliminado 
            print("\nEn el campo C está el Objetivo eliminado")
            print("No se realizó ninguna acción")
            print("Costo actual: " + str(costo))

    # Si el estado es 0 el objetivo A está eliminado
    elif estado_objetivo1 == '0':
        print("\nEn el campo A está el Objetivo eliminado")
        # Si el estado es 1 el objetivo B no está eliminado
        if estado_objetivo2 == '1':
            print("\nEn el campo B está el Objetivo no eliminado")
            # Proyectil se dirige al campo B
            print("Dirigiendose al campo B")
            print("Costo actual: " + str(costo))
            costo += 1  #Costo creciente 
            print("Costo actual: " + str(costo))
            # Eliminar el objetivo del campo B
            meta_estado['B'] = '0' # Cambiar estado del objetivo B a 0
            costo += 1 # Costo creciente
            # Imprimir costo actual y eliminación del objetivo en el campo B
            print("Eliminando Objetivo del campo B")
            print("Costo actual: " + str(costo))
        else:
            # Caso contrario, el Objetivo está eliminado 
            print("\nEn el campo B está el Objetivo eliminado")
            print("No se realizó ninguna acción")
            print("Costo actual: " + str(costo))

        # Si el estado es 1 el objetivo C no está eliminado
        if estado_objetivo3 == '1':
            print("\nEn el campo C está el Objetivo no eliminado")
            print("Dirigiendose al campo C")
            costo += 1  #Costo creciente
            print("Costo actual: " + str(costo))
            # Eliminar el objetivo del campo C
            meta_estado['C'] = '0' #Convirtiendo el estado del objetivo en 0
            costo += 1 # Costo creciente
            # Imprimir costo actual y eliminación del objetivo en el campo C
            print("Eliminando Objetivo en el campo C")
            print("Costo actual: " + str(costo))
        else:
            # Caso contrario, el Objetivo está eliminado 
            print("\nEn el campo C está el Objetivo eliminado")
            print("No se realizó ninguna acción")
            print("Costo actual: " + str(costo))
    else:
        # Valida que el estado ingresado sea 1 o 0
        print("Estado no válido")

    # Imprimir estado de la meta
    print("\nEstado de la meta: ")
    print(meta_estado)
    # Imprimir el costo de las acciones realizadas
    print("Medida de desempeño: " + str(costo))

def ubicacion_objetivoB():
    costo = 0 # Inicialización de costo
    estado_objetivo1 = input("Ingrese el estado de " + ubicacion_objetivo +
                             ": ")  # Estado de Ubicacion A
    estado_objetivo2 = input(
        "Ingrese el estado de A:  ")  # Estado de ubicacion B
    estado_objetivo3 = input(
        "Ingrese el estado de C: ")  # Estado de ubicacion C
    print('Meta deseada: ' + str(meta_estado) + ' deben ser eliminados')

    print("\nEl objetivo se coloca en el campo B")
    # Si el estado del objetivo es 1 el objetivo no está eliminado 
    if estado_objetivo1 == '1':
        print("\nEn el campo B está el Objetivo no eliminado")
        meta_estado['B'] = '0' # Convertir el estado del objetivo en 0
        costo += 1 # Costo creciente
        # Imprimir costo actual y eliminación del objetivo en el campo B
        print("Eliminando Objetivo en el campo B")
        print("Costo actual: " + str(costo))

        # Si el estado del objetivo es 1 el objetivo del campo A no está eliminado
        if estado_objetivo2 == '1':
            print("\nEn el campo A está el Objetivo no eliminado")
            # Proyectil se dirige al campo A
            print("Dirigiendose a la ubicación A")
            costo += 1 # Costo creciente
            print("Costo actual: " + str(costo))
            # Convertir el estado del objetivo del campo A en 0
            meta_estado['A'] = '0'
            costo += 1
            # Imprimir costo actual y eliminación del objetivo en el campo A
            print("Eliminando Objetivo en el campo A")
            print("Costo actual: " + str(costo))
        else:
            # Caso contrario, el Objetivo del campo A está eliminado
            print("\nEn el campo A está el Objetivo eliminado")
            print("No se realizó ninguna acción")
            print("Costo actual: " + str(costo))

        # Si el estado del objetivo es 1 el objetivo del campo C no está eliminado
        if estado_objetivo3 == '1':
            print("\nEn la ubicación C está el Objetivo no eliminado")
            # Proyectil se dirige al campo C
            print("Dirigiendose al campo C")
            costo += 1 # Costo creciente
            print("Costo actual: " + str(costo))
            # Convertir el estado del objetivo del campo C en 0
            meta_estado['C'] = '0'
            costo += 1  # Costo creciente
            print("Eliminando Objetivo en el campo C")
            print("Costo actual: " + str(costo))
        else:
            # Caso contrario, el Objetivo del campo C está eliminado
            print("\nEn el campo C está el Objetivo eliminado")
            print("No se realizó ninguna acción")
            print("Costo actual: " + str(costo))

    # Si el estado del objetivo es 0 el objetivo está eliminado
    elif estado_objetivo1 == '0':
        print("\nEn el campo B está el Objetivo eliminado")
        # Si el estado del objetivo es 1 el objetivo del campo A no está eliminado
        if estado_objetivo2 == '1':
            print("\nEn el campo A está el Objetivo no eliminado")
            # Proyectil se dirige al campo A
            print("Dirigiendose al campo A")
            costo += 1 # Costo creciente
            print("Costo actual: " + str(costo))
            meta_estado['A'] = '0' # Convertir el estado del objetivo en 0
            costo += 1
            print("Eliminando Objetivo en el campo A")
            print("Costo actual: " + str(costo))
        else:
            # Caso contrario, el Objetivo del campo A está eliminado
            print("\nEn el campo A está el Objetivo eliminado")
            print("No se realizó ninguna acción")
            print("Costo actual: " + str(costo))

        # Si el estado del objetivo es 1 el objetivo del campo C no está eliminado
        if estado_objetivo3 == '1':
            print("\nEn el campo C está el Objetivo no eliminado")
            # Proyectil se dirige al campo C
            print("Dirigiendose al campo C")
            costo += 1
            print("Costo actual: " + str(costo))
            # Convertir el estado del objetivo del campo C en 0
            meta_estado['C'] = '0'
            costo += 1
            # Imprimir costo actual y eliminación del objetivo en el campo C
            print("Eliminando Objetivo en el campo C")
            print("Costo actual: " + str(costo))
        else:
            # Caso contrario, el Objetivo del campo C está eliminado
            print("\nEn el campo C está el Objetivo eliminado")
            print("No se realizó ninguna acción")
            print("Costo actual: " + str(costo))
    else:
        # Valida que el estado del objetivo sea 1 o 0
        print("Estado no válido")

    # Imprimir costo final y estado final del objetivo en el campo B
    print("\nEstado de la meta: ")
    print(meta_estado)
    print("Medida de desempeño: " + str(costo))