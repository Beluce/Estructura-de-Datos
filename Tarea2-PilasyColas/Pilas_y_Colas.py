from collections import deque

class Pila:
    def __init__(self):
        self.objetos=[]

    def PilaVacia(self):
        return len(self.objetos) == 0 

    def push(self, valor):
        self.objetos.append(valor)

    def desapilar(self): #pop
        try:
            return self.objetos.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
        
    def peek(self):
        if not self.PilaVacia():
            return self.objetos[-1]
        else:
            return None
        
class Cola:
    def __init__(self):
        self.objetos = deque()

    def enqueue(self, objeto):
        self.objetos.append(objeto)
    
    def dequeue(self):
        if not self.colaVacia():
            return self.objetos.popleft()
        else:
            return None
        
    def peek(self):
        if not self.colaVacia():
            return self.objetos[0]
        else:
            return None
        
    def colaVacia(self):
        return len(self.objetos) == 0
    

    
pila = Pila()
pila.push(1)
pila.push(2)
pila.desapilar
pila.push(3)
pila.peek
print("El tope de la pila es:", pila.peek())

cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.dequeue
cola.enqueue(3)
cola.peek
print("Frente de la cola:", cola.peek())