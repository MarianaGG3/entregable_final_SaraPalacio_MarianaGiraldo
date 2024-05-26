from Modelo import Paciente
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog,QMessageBox
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi


class VentanaIngreso(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('login.ui',self)
        
        self.usuario.clicked.connect(self.validar_usuario)
        self.contrasena.clicked.connect(self.validar_contrasena)
        # self.usuario_valido = False
        # self.contrasena_valida = False

    def validar_usuario(self):
        usuario = self.usuarioLineEdit.text()

        if usuario == "admin123":
            self.usuario_valido = True
            QMessageBox.information(self,"Usuario correcto")
        else:
            self.usuario_valido = False
            QMessageBox.critical(self, "Usuario incorrecto. Por favor, intente de nuevo.")
        
        self.verificar_acceso()

    