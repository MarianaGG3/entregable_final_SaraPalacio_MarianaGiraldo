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
        self.setup()