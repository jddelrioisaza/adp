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

        self.__grafo = nx.DiGraph()
        self.__grafo.add_nodes_from({'p', 'q', 'r'})
        self.__grafo.add_weighted_edges_from(self.__generarAristas())

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

    def __a_b_ba(self):

        self.pila.desapilar()
        self.pila.apilar('b')
        self.pila.apilar('a')

        self.__actualizarAristas('p', 'p')

        self.__activarEstadoP()

    def __a_a_aa(self):

        self.pila.desapilar()
        self.pila.apilar('a')
        self.pila.apilar('a')

        self.__actualizarAristas('p', 'p')

        self.__activarEstadoP()

    def __a_z_za(self):

        self.pila.desapilar()
        self.pila.apilar('Z')
        self.pila.apilar('a')

        self.__actualizarAristas('p', 'p')

        self.__activarEstadoP()

    # TRANSICIONES CON B

    def __b_b_bb(self):

        self.pila.desapilar()
        self.pila.apilar('b')
        self.pila.apilar('b')

        self.__actualizarAristas('p', 'p')

        self.__activarEstadoP()

    def __b_a_ab(self):

        self.pila.desapilar()
        self.pila.apilar('a')
        self.pila.apilar('b')

        self.__actualizarAristas('p', 'p')

        self.__activarEstadoP()

    def __b_z_zb(self):

        self.pila.desapilar()
        self.pila.apilar('Z')
        self.pila.apilar('b')

        self.__actualizarAristas('p', 'p')

        self.__activarEstadoP()

    # TRANSICIONES QUE LLEVAN A Q

    def __b_b_n(self):

        self.pila.desapilar()

        self.__activarEstadoQ()

    def __a_a_n(self):

        self.pila.desapilar()

        self.__activarEstadoQ()

    # TRANSICIONES QUE LLEVAN A R

    def __n_z_z(self):

        self.pila.desapilar()
        self.pila.apilar('Z')

        self.__actualizarAristas('q', 'r')

        self.__activarEstadoR()

    # VALIDAR

    def __iniciarGrafo(self, velocidad):

        nx.draw(self.__grafo, self.posVertices, with_labels = True, node_color = "red")
        nx.draw_networkx_edges(self.__grafo, self.posVertices)
        plt.pause(1 / velocidad)

    def __actualizarNodos(self, estado, velocidad):

        if (estado != 'r'):

            nx.draw(self.__grafo, self.posVertices, with_labels = True, node_color = ['blue' if node == estado else 'red' for node in self.__grafo.nodes()])
            plt.pause(1 / velocidad)

        else:

            nx.draw(self.__grafo, self.posVertices, with_labels = True, node_color = ['blue' if node == estado else 'red' for node in self.__grafo.nodes()])
            plt.pause(1 / velocidad)

    def __actualizarAristas(self, estadoInicial, estadoFinal):

        pass

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
                        self.__a_b_ba()

                    elif self.pila.tope() == 'a':

                        if (i < (longitud / 2) + 1):

                            self.__actualizarNodos('p', velocidad)
                            self.__a_a_aa()

                        elif (i == (longitud / 2) + 1):

                            self.__actualizarNodos('p', velocidad)
                            self.__a_a_n()

                    elif self.pila.tope() == 'Z':

                        self.__actualizarNodos('p', velocidad)
                        self.__a_z_za()

                elif caracter == 'b':

                    if self.pila.tope() == 'b':

                        if (i < (longitud / 2) + 1):

                            self.__actualizarNodos('p', velocidad)
                            self.__b_b_bb()

                        elif (i == (longitud / 2) + 1):

                            self.__actualizarNodos('p', velocidad)
                            self.__b_b_n()

                    elif self.pila.tope() == 'a':

                        self.__actualizarNodos('p', velocidad)
                        self.__b_a_ab()

                    elif self.pila.tope() == 'Z':

                        self.__actualizarNodos('p', velocidad)
                        self.__b_z_zb()

            elif self.__getEstadoQ():

                if caracter == 'b':

                    if self.pila.tope() == 'b':

                        self.__actualizarNodos('q', velocidad)
                        self.__b_b_n()

                    else:

                        break

                elif caracter == 'a':

                    if self.pila.tope() == 'a':

                        self.__actualizarNodos('q', velocidad)
                        self.__a_a_n()

                    else:

                        break

                elif caracter == ' ':

                    if self.pila.tope() == 'Z' and self.__getEstadoQ():

                        self.__actualizarNodos('q', velocidad)
                        self.__n_z_z()
                        self.__actualizarNodos('r', velocidad)

            i = i + 1

            self.__iniciarGrafo(velocidad)

        plt.close()

        if self.__getEstadoR():

            self.__reiniciarEstados()
            self.__procesarVoz("LA CADENA FUE ACEPTADA POR EL AUTÓMATA.")
            return True

        else:

            self.__reiniciarEstados()
            self.__procesarVoz("LA CADENA NO FUE ACEPTADA POR EL AUTÓMATA.")
            return False

    def __generarAristas(self):

        aristas = set()

        aristas.add(('p', 'p', 'a'))
        aristas.add(('p', 'q', 'b'))
        aristas.add(('q', 'q', 'c'))
        aristas.add(('q', 'r', 'd'))

        return aristas

    def __procesarVoz(self, texto):

        objeto = gTTS(text = texto, lang= "es", slow = False)
        objeto.save("mensaje.mp3")

        playsound("mensaje.mp3", block = True)

        os.remove("mensaje.mp3")
