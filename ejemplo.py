class Persona():
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = float(balance)


    def __str__(self):
        return f"El cliente es: {self.nombre} {self.apellido}, su nro de cuenta es: {self.numero_cuenta} y su saldo es: {float(self.balance)}"

    def depositar(self):
        monto_depositar = float(input(f'Introduzca el monto a depositar: '))
        self.balance += monto_depositar
        print(f'Su balance nuevo es: {self.balance}')

    def retirar(self):
        monto_retirar = float(input(f'Introduzca el monto a retirar: '))
        if (self.balance - monto_retirar) < 0:
            print("No puede retirar más del disponible")
        else:
            self.balance -= monto_retirar
        print(f'Su balance nuevo es: {self.balance}')

def crear_cliente(nombre1, apellido1, numero_cuenta1, balance1):
    return Cliente(nombre1,apellido1,numero_cuenta1, balance1)

#Inicio Programa
nombre1 = input('Introduzca nombre cliente: ')
apellido1 = input('Introduzca apellido cliente: ')
numero_cuenta1 = input('Introduzca numero cuenta: ')
balance1 = input('Introduzca balance inicial: ')
mi_cliente = crear_cliente(nombre1,apellido1,numero_cuenta1,balance1)

#menu opciones
opcion = 'x'
while opcion != 4:
    print('*' * 20)
    print('Menu Principal')
    print('1. Mostrar cliente')
    print('2. Depositar')
    print('3. Retirar')
    print('4. Salir')
    opcion=input("Seleccione opción: ")
    match opcion:
        case '1':
            print(mi_cliente)
        case '2':
            mi_cliente.depositar()
        case '3':
            mi_cliente.retirar()
        case '4':
            print('Ha finalizado el programa...')
            break







