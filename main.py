import os
import messages
from tasks_list import TasksList

def main_menu():
    print('*' * 50)
    print('\n*** Menu Principal ***')
    print('1. Agregar nueva tarea')
    print('2. Marcar tarea como completada')
    print('3. Mostrar tareas')
    print('4. Eliminar tarea')
    print('0. Salir')
    print('*' * 50)

def enter_task():
    task_name = ''
    while task_name == '':
        task_name = input("Ingrese la nueva tarea: ")        
        if len(task_name) == 0:
            messages.errors('03')    
    tasks_list.add_task(task_name)

def select_complete_task():
    index = int(input("Ingrese el índice a completar: ")) 
    index-=1
    tasks_list.complete_task(index)

def select_delete_task():
    index = int(input("Ingrese el índice de la tarea a eliminar: ")) 
    index-=1
    tasks_list.delete_task(index)


def main():    
    os.system('cls')
    while True:    
        main_menu()
        try:
            opcion=int(input("Seleccione opción: "))
            match opcion:
                case 1:
                    enter_task()
                case 2:
                    tasks_list.show_tasks()                    
                    if tasks_list.list_size() > 0:
                        select_complete_task()  
                case 3:
                    tasks_list.show_tasks()
                case 4:
                    tasks_list.show_tasks()                    
                    if tasks_list.list_size() > 0:
                        select_delete_task()  
                case 0:
                    print('Ha finalizado el programa...')
                    break
                case _:
                    messages.errors('01')
        except ValueError:
            messages.errors('02')
                

tasks_list = TasksList()        
if __name__ == "__main__":
    main()