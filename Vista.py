from Modelo import Paciente
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox,QLabel, QWidget
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator, QFont
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi


class VentanaIngreso(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('login.ui',self)
        
        self.ingresar.clicked.connect(self.validar_login)
        # self.label1=QLabel(None, self)
        # fuente = QFont()
        # fuente.setPointSize(14)  
        # self.label.setFont(fuente)
        

    
    def validar_login(self):
        usuario = self.usuario.text()
        contrasena = self.contrasena.text()
        #vista_=VentanaIngreso()


        if usuario == "admin123" and contrasena == "contrasena123":
            QMessageBox.information(self, "Éxito", "Usuario y contraseña correctos")
            self.quit_ventanaingreso=QWidget.QDialog("ingresar",self)
            self.quit_ventanaingreso.clicked(QWidget.qApp.quit)
        else:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos. Por favor, intente de nuevo.")
         

class VentanaDatosPac(QDialog):
    def __init__(self, parent=None):
        super(VentanaDatosPac,self).__init__(parent)
        loadUi('ventana_datos_paciente',self)
        self.ventanaing= parent

        self.agregar.clicked.connect(self.validarpac)

        def validarpac(self):
            pass