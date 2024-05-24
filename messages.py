"""Diccionario que guarda los mensajes de error"""
errors_dictionary = {
    '01':'Opción inválida...',
    '02':'Debe ingresar un número... ',
    '03':'Cadena no puede estar vacia... ',
    '04':'El índice ingresado no es válido... ',
    '05':'La lista de tareas está vacía...',
    '99':'Código de error no codificado'
}

"""Diccionario que gestiona los mensajes en la aplicación"""
messages_dictionary = {
    '01':"La tarea 'variable_text' se ha agregado a la lista de tareas",
    '02':"La tarea 'variable_text' se ha marcado como completada.",
    '03':"La tarea 'variable_text' se ha eliminado.",
    '99':"Código de mensaje no codificado"

}

"""Muestra los mensajes de error"""
def errors(error_number):
    try:
        print(errors_dictionary[error_number])
    except:
        print(errors_dictionary['99'])


"""Muestra los mensajes de la aplicación"""
def messages(message_number,variable):
    try:        
        print(messages_dictionary[message_number].replace("variable_text", variable ))
    except:
        print(messages_dictionary['99'])