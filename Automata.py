import os

from Pila import Pila

from gtts import gTTS
from playsound import playsound

import networkx as nx
import matplotlib.pyplot as plt


class Automata:

    def __init__(self):

        self.pila = Pila()
        self.resultado = []
        self.transiciones = []
        self.estados = [True, False, False]

        self.posVertices = {

        'p': (2, 1),
        'q': (1, 1),
        'r': (1, -1)

        }

        self.edgeColors = {

            ('p', 'p'): 'b',
            ('p', 'q'): 'b',
            ('q', 'q'): 'b',
            ('q', 'r'): 'b'

        }

        self.__grafo = nx.DiGraph()
        self.__grafo.add_nodes_from({'p', 'q', 'r'})
        self.__grafo.add_edges_from(self.__generarAristas())

        plt.rcParams['toolbar'] = 'None'

    def __getEstadoP(self):

        return self.estados[0]

    def __getEstadoQ(self):

        return self.estados[1]

    def __getEstadoR(self):

        return self.estados[2]

    def __activarEstadoP(self):

        self.estados[0] = True
        self.estados[1] = False
        self.estados[2] = False

    def __activarEstadoQ(self):

        self.estados[0] = False
        self.estados[1] = True
        self.estados[2] = False

    def __activarEstadoR(self):

        self.estados[0] = False
        self.estados[1] = False
        self.estados[2] = True

    def __reiniciarEstados(self):

        self.estados = [True, False, False]

    # TRANSICIONES CON A

    def __a_b_ba(self, velocidad):

        self.pila.desapilar()
        self.pila.apilar('b')
        self.pila.apilar('a')

        self.__actualizarAristas('p', 'p', velocidad)

        self.__activarEstadoP()

    def __a_a_aa(self, velocidad):

        self.pila.desapilar()
        self.pila.apilar('a')
        self.pila.apilar('a')

        self.__actualizarAristas('p', 'p', velocidad)

        self.__activarEstadoP()

    def __a_z_za(self, velocidad):

        self.pila.desapilar()
        self.pila.apilar('Z')
        self.pila.apilar('a')

        self.__actualizarAristas('p', 'p', velocidad)

        self.__activarEstadoP()

    # TRANSICIONES CON B

    def __b_b_bb(self, velocidad):

        self.pila.desapilar()
        self.pila.apilar('b')
        self.pila.apilar('b')

        self.__actualizarAristas('p', 'p', velocidad)

        self.__activarEstadoP()

    def __b_a_ab(self, velocidad):

        self.pila.desapilar()
        self.pila.apilar('a')
        self.pila.apilar('b')

        self.__actualizarAristas('p', 'p', velocidad)

        self.__activarEstadoP()

    def __b_z_zb(self, velocidad):

        self.pila.desapilar()
        self.pila.apilar('Z')
        self.pila.apilar('b')

        self.__actualizarAristas('p', 'p', velocidad)

        self.__activarEstadoP()

    # TRANSICIONES QUE LLEVAN A Q

    def __b_b_n(self):

        self.pila.desapilar()

        self.__activarEstadoQ()

    def __a_a_n(self):

        self.pila.desapilar()

        self.__activarEstadoQ()

    # TRANSICIONES QUE LLEVAN A R

    def __n_z_z(self, velocidad):

        self.pila.desapilar()
        self.pila.apilar('Z')

        self.__actualizarAristas('q', 'r', velocidad)

        self.__activarEstadoR()

    # VALIDAR

    def __iniciarGrafo(self, velocidad):

        nx.draw(self.__grafo, self.posVertices, with_labels = True, node_color = "red", node_size = 500)
        nx.draw_networkx_edges(self.__grafo, self.posVertices)
        plt.pause(1 / velocidad)

    def __actualizarNodos(self, estado, velocidad):

        if (estado != 'r'):

            nx.draw(self.__grafo, self.posVertices, with_labels = True, node_color = ['blue' if node == estado else 'red' for node in self.__grafo.nodes()], node_size = 500)
            plt.pause(1 / velocidad)
            self.__iniciarGrafo(velocidad)

        else:

            nx.draw(self.__grafo, self.posVertices, with_labels = True, node_color = ['blue' if node == estado else 'red' for node in self.__grafo.nodes()], node_size = 500)
            plt.pause(1 / velocidad)
            self.__iniciarGrafo(velocidad)

    def __actualizarAristas(self, estadoInicial, estadoFinal, velocidad):

        nx.draw_networkx_edges(self.__grafo, self.posVertices, edge_color = ['blue' if edge == (estadoInicial, estadoFinal) else 'black' for edge in self.__grafo.edges()])
        plt.pause(1 / velocidad)

    def procesar(self, palabra, velocidad):

        plt.close()

        self.__iniciarGrafo(velocidad)

        longitud = len(palabra)
        i = 1
        palabra = palabra + ' '

        for caracter in palabra:

            if (caracter != 'a' and caracter != 'b' and caracter != ' '):

                return False

            elif self.__getEstadoP():

                if caracter == 'a':

                    if self.pila.tope() == 'b':

                        self.__actualizarNodos('p', velocidad)
                        self.__a_b_ba(velocidad)

                    elif self.pila.tope() == 'a':

                        if (i < (longitud / 2) + 1):

                            self.__actualizarNodos('p', velocidad)
                            self.__a_a_aa(velocidad)

                        elif (i == (longitud / 2) + 1):

                            self.__actualizarNodos('p', velocidad)
                            self.__a_a_n()
                            self.__actualizarAristas('p', 'q', velocidad)

                    elif self.pila.tope() == 'Z':

                        self.__actualizarNodos('p', velocidad)
                        self.__a_z_za(velocidad)

                elif caracter == 'b':

                    if self.pila.tope() == 'b':

                        if (i < (longitud / 2) + 1):

                            self.__actualizarNodos('p', velocidad)
                            self.__b_b_bb(velocidad)

                        elif (i == (longitud / 2) + 1):

                            self.__actualizarNodos('p', velocidad)
                            self.__b_b_n()
                            self.__actualizarAristas('p', 'q', velocidad)

                    elif self.pila.tope() == 'a':

                        self.__actualizarNodos('p', velocidad)
                        self.__b_a_ab(velocidad)

                    elif self.pila.tope() == 'Z':

                        self.__actualizarNodos('p', velocidad)
                        self.__b_z_zb(velocidad)

            elif self.__getEstadoQ():

                if caracter == 'b':

                    if self.pila.tope() == 'b':

                        self.__actualizarNodos('q', velocidad)
                        self.__b_b_n()
                        self.__actualizarAristas('q', 'q', velocidad)

                    else:

                        break

                elif caracter == 'a':

                    if self.pila.tope() == 'a':

                        self.__actualizarNodos('q', velocidad)
                        self.__a_a_n()
                        self.__actualizarAristas('q', 'q', velocidad)

                    else:

                        break

                elif caracter == ' ':

                    if self.pila.tope() == 'Z' and self.__getEstadoQ():

                        self.__actualizarNodos('q', velocidad)
                        self.__n_z_z(velocidad)
                        self.__actualizarNodos('r', velocidad)

            i = i + 1

            self.__iniciarGrafo(velocidad)

        plt.close()

        if self.__getEstadoR():

            self.__reiniciarEstados()
            #self.__procesarVoz("LA CADENA FUE ACEPTADA POR EL AUTÓMATA.")
            return True

        else:

            self.__reiniciarEstados()
            #self.__procesarVoz("LA CADENA NO FUE ACEPTADA POR EL AUTÓMATA.")
            return False

    def __generarAristas(self):

        aristas = set()

        aristas.add(('p', 'p'))
        aristas.add(('p', 'q'))
        aristas.add(('q', 'q'))
        aristas.add(('q', 'r'))

        return aristas

    def __procesarVoz(self, texto):

        objeto = gTTS(text = texto, lang= "es", slow = False)
        objeto.save("mensaje.mp3")

        playsound("mensaje.mp3", block = True)

        os.remove("mensaje.mp3")
