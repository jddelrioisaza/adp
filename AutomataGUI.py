from PySide6.QtWidgets import *
from PySide6.QtCore import *

from Automata import Automata

class AutomataGUI(QMainWindow):

    def __init__(self):

        super().__init__()

        self.__automata = Automata()

        self.__crearInterfaz()

    def __crearInterfaz(self):

        # NOMBRE Y TAMAÑO DE LA VENTANA
        self.setWindowTitle(("Autómata"))

        # WIDGET PRNCIPAL
        widget = QWidget()
        self.setCentralWidget(widget)

        # LAYOUT PRINCIPAL
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # QLABEL PARA MOSTRAR MENSAJE
        label_velocidad = QLabel(("INTRODUZCA UNA CADENA:"))
        layout.addWidget(label_velocidad)

        # QLINEEDIT PARA INGRESAR LA CADENA
        self.__linee_cadena = QLineEdit()
        layout.addWidget(self.__linee_cadena)

        label_cadena = QLabel(("VELOCIDAD:"))
        layout.addWidget(label_cadena)

        self.__deslizador = QSlider(Qt.Horizontal)
        self.__deslizador.setMinimum(1)
        self.__deslizador.setMaximum(5)
        self.__deslizador.setValue(1)
        layout.addWidget(self.__deslizador)

        # BOTÓN PARA PROCESAR
        btn_procesar = QPushButton(("PROCESAR"))
        btn_procesar.clicked.connect(self.__procesar)
        layout.addWidget(btn_procesar)

    def __procesar(self):

        if self.__automata.procesar(self.__linee_cadena.text(), self.__deslizador.value()):

            QMessageBox.information(self, "RESULTADO", "LA CADENA FUE ACEPTADA POR EL AUTÓMATA.")

        else:

            QMessageBox.information(self, "RESULTADO", "LA CADENA NO FUE ACEPTADA POR EL AUTÓMATA.")
