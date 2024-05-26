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
        
        self.ingresar.clicked.connect(self.validar_login)
    
    def validar_login(self):
        usuario = self.usuario.text()
        contrasena = self.contrasena.text()
        #vista_=VentanaIngreso()


        if usuario == "admin123" and contrasena == "contrasena123":
            QMessageBox.information(self, "Éxito", "Usuario y contraseña correctos")
            
        else:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos. Por favor, intente de nuevo.")
         