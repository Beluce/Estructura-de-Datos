class Node():
    def __init__(self, value=None, reference=None): #La referencia siempre apunta al frente
        if value is not None:
            self.value = value
        else:
            self.value = None
        if reference is not None:
            self.reference = reference
        else:
            self.reference = None

class DoubleNode:
    def __init__(self, value=None, next_node=None, prev_node=None):
        if value is not None:
            self.value = value

        self.siguiente = next_node

        if prev_node is not None:
            self.anterior = prev_node

class CircularNode():
    def __init__(self, data):
        if data is not None:
            self.data = data
        else:
            self.data = None
        self.next = None