from Pilas_y_Colas import *

#Creamos una Pila y una Cola iniciales con las que trabajara nuestro menu :)

pila = Pila()
cola = Cola()

menu = 0

while True:
    print("\nMenú Pilas y Colas")
    print("1) Pila")
    print("2) Cola")
    print("3) Salir")

    try:
        menu = int(input("Introduce la operacion: "))
    except ValueError:
        print("Los caracteres no estan permitidos")
        continue

    if menu == 1:
        while True:
            print("\nMenu para la Pila")
            print("1) Peek")
            print("2) Push")
            print("3) Pop")
            print("4) Mostrar pila actual")
            print("5) Regresar al Menu Principal")

            try:
                menu_pila = int(input("Introduce la operacion de pila: "))
            except ValueError:
                print("Los caracteres no estan permitidos")
                continue

            if menu_pila == 1:
                print("Elemento en la cima de la pila:", pila.peek())
            elif menu_pila == 2:
                elemento = input("Introduce el elemento a agregar: ")
                print("Elemento agregado:", pila.push(elemento))
            elif menu_pila == 3:
                print("Elemento retirado:", pila.pop())
            elif menu_pila == 4:
                print("Pila actual:", pila.mostrar())
            elif menu_pila == 5:
                break
            else:
                print("Opción no válida. Por favor intenta de nuevo.")

    elif menu == 2:
        while True:
            print("\nMenú de Cola")
            print("1) Peek")
            print("2) Enqueue (Agregar)")
            print("3) Dequeue (Retirar)")
            print("4) Mostrar cola actual")
            print("5) Regresar")

            try:
                menu_cola = int(input("Introduce la operacion de cola: "))
            except ValueError:
                print("Los caracteres no estan permitidos")
                continue

            if menu_cola == 1:
                print("Primer elemento de la cola:", cola.peek())
            elif menu_cola == 2:
                elemento = input("Introduce el elemento a agregar: ")
                print("Elemento agregado:", cola.enqueue(elemento))
            elif menu_cola == 3:
                print("Elemento retirado:", cola.dequeue())
            elif menu_cola == 4:
                print("Cola actual:", cola.mostrar())
            elif menu_cola == 5:
                break
            else:
                print("Opción no válida. Por favor intenta de nuevo.")

    elif menu == 3:
        print("Gracias por usar la aplicación")
        break
    else:
        print("Opción no válida. Por favor intenta de nuevo.")