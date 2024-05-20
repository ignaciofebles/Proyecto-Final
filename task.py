class Task:    
    
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete_task(self):
        self.completed = True

    def __str__(self):
        status = "Completada" if self.completed else "Pendiente"
        return f"{self.name} - {status}"