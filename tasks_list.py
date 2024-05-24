"""Se importa la clase tarea desde el fichero task.py que es la clase con los atributos de la tarea"""
"""Se importa el fichero de mensajes para gestionar los mensajes"""
from task import Task
import messages

class TasksList:
    """Esta es la clase lista de tareas que te gestiona la inicialización de la clase, agregar tarea, completar tarea, mostrar las tareas y eliminar las tareas"""
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        new_task = Task(task_name)
        self.tasks.append(new_task)        
        messages.messages('01',task_name)

    def complete_task(self, index):
        try:
            self.tasks[index].complete_task()            
            messages.messages('02',self.tasks[index].name)
        except IndexError:
            messages.errors('04')

    def show_tasks(self):
        print('-' * 50)        
        print("\n--- Lista de tareas ---")
        if not self.tasks:
            messages.errors('05')            
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
        print('-' * 50)

    def delete_task(self, index):
        try:
            delete_task = self.tasks.pop(index)            
            messages.messages('03',delete_task.name)
        except IndexError:
            messages.errors('04')

    def list_size(self):
        return len(self.tasks)
    
