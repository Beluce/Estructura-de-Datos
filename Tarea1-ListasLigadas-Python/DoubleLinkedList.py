from Node import DoubleNode

class DoubleLinkedList:
    def __init__(self, values=None):
        self.header = DoubleNode()
        self.cola = self.header #Puntero al final de la lista

        if values is not None:
            for i in values:
                self.add_end(i)

    def add_end(self, value): #Metodo para anadir un valor al final de la lista
        NodoFinal = DoubleNode(value, None, self) #Creamos el nodo que ira al final de la lista

        self.cola.siguiente = NodoFinal
        self.cola = NodoFinal

    def add(self, index, value): #Metodo para anadir un valor en cualquier "index" de la lista

        posActual = self.header

        for i in range(index):
            if posActual.siguiente is None:
                raise IndexError("Indice fuera de los limites...")
            posActual = posActual.siguiente

        Nodo = DoubleNode(value, posActual.siguiente, posActual)
        if posActual.siguiente is not None:
            posActual.siguiente.anterior = Nodo
        posActual.siguiente = Nodo

    def print_data(self):
        posActual = self.header.siguiente
        while posActual:
            print(posActual.value, end= " <-> ")
            posActual = posActual.siguiente
        print()

    def print_reverso(self):
        posActual = self.cola
        while posActual is not self.header:
            print(posActual.value, end= " <-> ")
            posActual = posActual.anterior
        print()