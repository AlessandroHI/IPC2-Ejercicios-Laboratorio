
class Cliente():
    def __init__(self,nombre,telefono):
        self.nombre = nombre
        self.telefono = telefono

class Nodo():
    def __init__(self,dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class lista:
  def __init__(self):
    self.primero = None

  def insertar(self, data):
    if self.primero is None:
      self.primero = Nodo(dato=data)
      return 
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = Nodo(dato=data)

  def recorrer(self):
    print("-------- DATOS -----------")
    actual = self.primero
    while actual != None:
      print('Nombre:',actual.dato.nombre, "Telefonos:", actual.dato.telefono,"-->" )
      actual = actual.siguiente
    print("")

def ingresarDatos():
    nombre = input("Ingrese su nombre: ")
    telefono = input("Ingrese su numero de telefono: ")
    dato = Cliente(nombre,telefono)
    listac.insertar(dato)
    print("Datos almacenado con exito...")
    print("")



def mostrarDatos():
    listac.recorrer()

if __name__ == '__main__': #MAIN INICIO DEL PROGRAMA
   global listac
   listac = lista()


   print("--------- BIENVENIDO ---------")
   menuprincipal = int(input(
        "------- MENU PRINCIPAL------- \n 1- Ingresar Datos  \n 2- Mostrar Datos \n 3- Salir\nPor favor elija una opcion: \n"))
   while menuprincipal != 3:
 
    if menuprincipal == 1:
     ingresarDatos()

    elif menuprincipal == 2:
     mostrarDatos()  

    else:
     print("Opcion ingresa invalida!")

    menuprincipal = int(input(
        "------- MENU PRINCIPAL------- \n 1- Ingresar Datos  \n 2- Mostrar Datos \n 3- Salir \nPor favor elija una opcion: \n"))

