#Para implementar Pilas y Colas podemos usar lo aprendido de Nodos y Listas Enlazadas

class Nodo: 

    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pila:

    def __init__(self):
        self.tope = None #Pila vacia

    def peek(self):
        if not self.tope:
            return None
        return self.tope.valor #Regresa la referencia al tope de la pila

    def push(self, elemento):
        nodo_nuevo = Nodo(elemento) #Instanciamos un nuevo nodo cuando se agrega un elemento a la pila


        nodo_nuevo.next = self.tope #Ya que agregamos el nodo nuevo, el nodo siguiente contiene la referencia del tope de la pila, 
                                    #asi que de esta manera lo confirmamos, para posteriormente actualizar el tope para que apunte al nuevo nodo,
                                    #y este se convierta en el elemento superior de la pila


        self.tope = nodo_nuevo #El nuevo nodo se convierte en el tope

        return elemento #Muestra el elemento agregado

    def pop(self):
        if not self.tope:
            return None
        nodo_a_eliminar = self.tope #Para eliminar un elemento de la pila, debemos situarnos al principio (tope) de esta:
        self.tope = self.tope.next #Le asignamos la referencia del tope al siguiente elemento en la pila
        return nodo_a_eliminar.valor #De esta manera, automaticamente eliminamos el enlace y, en consecuencia, regresamos
                                    #el valor que seguia en la pila, convirtiendose en el nuevo tope
                                    #(Last in - First Out)

    def mostrar(self): #Mostramos los elementos contenidos en la Pila gracias a un array que los almacene
        elementos = []
        actual = self.tope
        while actual:
            elementos.append(actual.valor)
            actual = actual.next
        return elementos

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None #Fila vacia, con ambas referencias en None

    def peek(self):
        if not self.frente:
            return None
        return self.frente.valor #El peek regresara el valor que esta hasta el frente de la fila, el primer valor en ser agregado

    # Enqueue agrega el valor deseado hasta el final de la cola
    def enqueue(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.final is None:  # Si nuestra fila esta vacia, el nuevo nodo apuntara a si mismo (sera la cola y el frente)
            self.frente = self.final = nuevo_nodo
        else:
            self.final.next = nuevo_nodo #Similar a las pilas, obtenemos la referencia del final de nuestra cola actual, y se la agregamos al nuevo nodo
            self.final = nuevo_nodo      #De esta manera, el elemento anterior se convierte en el siguiente, y el nuevo se convierte en el final
        return elemento

    # Dequeue remueve el valor al frente de la fila (First In - First Out)
    def dequeue(self):
        if not self.frente:
            return None
        nodo_dequeue = self.frente #Nuestro nodo a eliminar siempre sera el nodo al frente de la fila
        self.frente = self.frente.next #La referencia del nodo al frente se recorre al nodo siguiente a este
        if self.frente is None:  #En caso que la cola este vacia despues de la operacion, la referencia al final de la fila se vuelve None
            self.final = None
        return nodo_dequeue.valor
    
    def mostrar(self): #Para mostrar los elementos, se debe de crear un array para almacenar los nodos creados
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(actual.valor)
            actual = actual.next
        return elementos