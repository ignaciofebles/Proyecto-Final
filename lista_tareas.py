from tarea import Tarea

class ListaTareas:
    """Clase que gestiona una lista de tareas."""
    
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre_tarea):
        nueva_tarea = Tarea(nombre_tarea)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{nombre_tarea}' se ha agregado a la lista de tareas")

    def marcar_completada(self, posicion):
        try:
            self.tareas[posicion].marcar_completada()
            print(f"Tarea '{self.tareas[posicion].nombre}' marcada como completada.")
        except IndexError:
            print("Error: La posición ingresada no es válida.")

    def mostrar_tareas(self):
        print('-' * 50)        
        print("\n--- Lista de Tareas ---")
        if not self.tareas:
            print("La lista de tareas está vacía.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea}")
        print('-' * 50)

    def eliminar_tarea(self, posicion):
        """Elimina una tarea de la lista según su posición."""
        try:
            tarea_eliminada = self.tareas.pop(posicion)
            print(f"Tarea '{tarea_eliminada.nombre}' eliminada de la lista.")
        except IndexError:
            print("Error: La posición ingresada no es válida.")
