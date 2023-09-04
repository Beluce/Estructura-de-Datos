from Node import CircularNode

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        Nodo = CircularNode(data)
        if not self.head:
            self.head = Nodo
            Nodo.next = self.head  # Hacemos que el único nodo apunte a sí mismo
        else:
            posAct = self.head
            while posAct.next != self.head:
                posAct = posAct.next
            posAct.next = Nodo
            Nodo.next = self.head

    def display(self):
        if not self.head:
            return
        posAct = self.head
        while True:
            print(posAct.data, end=" -> ")
            posAct = posAct.next
            if posAct == self.head:
                break
        print(" (Regresa al principio, Nodo apuntador)")