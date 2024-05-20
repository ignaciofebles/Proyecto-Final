import os
from errores import errores
from lista_tareas import ListaTareas

def menu_principal():
    print('*' * 50)
    print('\n*** Menu Principal ***')
    print('1. Agregar nueva tarea')
    print('2. Marcar tarea como completada')
    print('3. Mostrar tareas')
    print('4. Eliminar tarea')
    print('0. Salir')
    print('*' * 50)

def ingresar_tarea():
    nombre_tarea = ''
    while nombre_tarea == '':
        nombre_tarea = input("Ingrese la nueva tarea: ")        
        if len(nombre_tarea) == 0:
            errores(3)    
    lista_tareas.agregar_tarea(nombre_tarea)

def seleccionar_completar_tarea():
    posicion = int(input("Ingrese el índice a completar: ")) - 1
    lista_tareas.marcar_completada(posicion)

def seleccionar_eliminar_tarea():
    posicion = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
    lista_tareas.eliminar_tarea(posicion)


def main():    
    os.system('cls')
    while True:    
        menu_principal()
        try:
            opcion=int(input("Seleccione opción: "))
            match opcion:
                case 1:
                    ingresar_tarea()
                case 2:
                    lista_tareas.mostrar_tareas()                    
                    if lista_tareas.tamano_lista() > 0:
                        seleccionar_completar_tarea()  
                case 3:
                    lista_tareas.mostrar_tareas()
                case 4:
                    lista_tareas.mostrar_tareas()                    
                    if lista_tareas.tamano_lista() > 0:
                        seleccionar_eliminar_tarea()  
                case 0:
                    print('Ha finalizado el programa...')
                    break
                case _:
                    errores(1)
        except ValueError:
            errores(2)
                

lista_tareas = ListaTareas()        
if __name__ == "__main__":
    main()