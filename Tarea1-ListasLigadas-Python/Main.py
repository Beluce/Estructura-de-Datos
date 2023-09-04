from SimpleLinkedList import SimpleLinkedList
from DoubleLinkedList import DoubleLinkedList
from CircularLinkedList import CircularLinkedList

# Crear una Lista Ligada Simple
ListaLigadaSimple = SimpleLinkedList()

# Agregar elementos a la lista ligada simple:
ListaLigadaSimple.add(1,1)
ListaLigadaSimple.add(2,2)
ListaLigadaSimple.add(3,3)
ListaLigadaSimple.add(4,4)

# Imprimir los valores de la lista ligada
ListaLigadaSimple.print_data()

#Las listas ligadas simples siempre agregan el dato de manera secuencial

#Crear una lista ligada doble:
ListaLigadaDoble = DoubleLinkedList()

# Agregar elementos a la lista ligada doble:
ListaLigadaDoble.add_end("esta")
ListaLigadaDoble.add_end("es")
ListaLigadaDoble.add_end("una")
ListaLigadaDoble.add_end("lista")
ListaLigadaDoble.add_end("ligada")
ListaLigadaDoble.add_end("doble")
ListaLigadaDoble.add_end(69)

ListaLigadaDoble.add(1, 4)
ListaLigadaDoble.add(2,5)
ListaLigadaDoble.add(5, 1204981243)

# Imprimir los valores de la lista ligada
ListaLigadaDoble.print_data()

#Imprimir los valores de la lista al reves
ListaLigadaDoble.print_reverso

#La lista ligada doble tiene la facilidad de crear nodos dentro de la lista 
# para manipular el orden de los datos con mayor facilidad

#Crear una lista ligada circular
ListaLigadaCircular = CircularLinkedList()

#Agregar elementos a la lista ligada circular:
ListaLigadaCircular = CircularLinkedList()

ListaLigadaCircular.add("Lista")
ListaLigadaCircular.add("Circular")
ListaLigadaCircular.add("Enlazada")
ListaLigadaCircular.add(":)")

ListaLigadaCircular.display()