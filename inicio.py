#menu opciones
opcion = 'x'
while opcion != 0:
    print('*' * 20)
    print('Menu Principal')
    print('1. Agregar nueva tarea')
    print('2. Marcar tarea como completada')
    print('3. Mostrar tareas')
    print('4. Eliminar tarea')
    print('0. Salir')
    opcion=input("Seleccione opción: ")
    match opcion:
        case '1':
            print('1')
        case '2':
            print('2')
        case '3':
            print('3')
        case '4':
            print('4')
        case '0':
            print('Ha finalizado el programa...')
            break
        
