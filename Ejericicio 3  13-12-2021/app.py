from os import access
from xml.etree import ElementTree
class Nodo():
    def __init__(self, valor=None, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente 

class Lista(Nodo):
    def __init__(self):
        super().__init__()
        self.cabeza = Nodo()
        self.contador = 0
        
    def insertar(self, nuevo_nodo):
        nodo = self.cabeza
        while(nodo.siguiente):
            nodo = nodo.siguiente
        nodo.siguiente = nuevo_nodo
        self.contador += 1


    def get(self, i):
        if (i >= self.contador):
            return None
        nodo = self.cabeza.siguiente
        n = 0
        while(nodo):
            if (n == i):
                return nodo
            nodo = nodo.siguiente
            n += 1

    def __getitem__(self, i):
        return self.get(i)

    def length(self):
        return self.contador

class Contacto(Lista):
    def __init__(self,nombre,apellido,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        super().__init__()


def lecturaXML():
  cont = 0
  ruta = input("Ingrese la ruta del archivo XML a cargar: ")
  archivoXML = ElementTree.parse(ruta)
  root = archivoXML.getroot()
  for elemento in root:
    pass
    for telefono in elemento.iter("telefono"):
      cel = telefono.text
    for nombre in elemento.iter("nombre"):
      name = nombre.text
    for apellido in elemento.iter("apellido"):
       lastname = apellido.text
       contacto = Contacto(name,lastname,cel)
       if cont == 0:
         listac.insertar(contacto)
         cont =+1 
       else:
         verificardato(contacto)
         cont =+1 
       

def verificardato(data):
  for i in range(listac.length()):
    if data.telefono  == listac[i].telefono:
      print("!ERROR Numero ya existente", data.telefono, "Nombre:", data.nombre)
      return
    else:
      listac.insertar(data)
      break
      


def printt(lista):
  for i in range(lista.length()):
    print("Nombre: ",lista[i].nombre,"Apellido:",lista[i].apellido,"Telefono:",lista[i].telefono)


if __name__ == '__main__': #MAIN INICIO DEL PROGRAMA
   global listac
   listac = Lista()


   print("--------- BIENVENIDO ---------")
   menuprincipal = (input(
        "------- MENU PRINCIPAL------- \n 1- Ingresar Datos  \n 2- Mostrar Datos \n 3- Salir\nPor favor elija una opcion: \n"))
   while menuprincipal != "3":
 
    if menuprincipal == "1":
     lecturaXML()

    elif menuprincipal == "2":
     printt(listac)  

    else:
     print("Opcion ingresa invalida!")

    menuprincipal = (input(
        "------- MENU PRINCIPAL------- \n 1- Ingresar Datos  \n 2- Mostrar Datos \n 3- Salir \nPor favor elija una opcion: \n"))

