class Pila:

    def __init__(self):

        self.pila = []
        self.pila.append('Z')

    def getPila(self):

        return self.pila

    def apilar(self, dato):

        self.pila.append(dato)

    def desapilar(self):

        if self.pilaVacia():

            print("¡LA PILA ESTÁ VACÍA!")

        else:

            return self.pila.pop()

    def tope(self):

        return self.pila[len(self.pila) - 1]

    def pilaVacia(self):

        if len(self.pila) == 0:

            return True

        else:

            return False
