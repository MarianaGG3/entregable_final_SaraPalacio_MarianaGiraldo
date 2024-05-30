
from Controlador import coordinador
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox,QLabel, QWidget, QLineEdit, QTableWidgetItem,QPushButton
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator, QFont
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi


class VentanaIngreso(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('login.ui',self)
        self.setup()

    def setup(self):
        
        self.ingresar.clicked.connect(self.validar_login)
        self.contrasena.setEchoMode(QLineEdit.Password)
        
        

    
    def validar_login(self):
        usuario = self.usuario.text()
        contrasena = self.contrasena.text()
        
        if usuario == "admin123" and contrasena == "contrasena123":
            self.ventana=VentanaDatosPac()
            self.ventana.show()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos. Por favor, intente de nuevo.")
         

class VentanaDatosPac(QDialog):
    def __init__(self):
        super(VentanaDatosPac, self).__init__()
        loadUi('ventana_datos.ui',self)
        
        self.controller=coordinador()
        self.setup()

    def setup(self):
       
        self.ingreso.clicked.connect(self.agregar_patient)
        self.busqueda.clicked.connect(self.buscar_patient)
        self.tabla.verticalHeader().setVisible(False)
        self.readPacient()
        self.tableUpdate()

    def readPacient(self):
        self.listPaciente= self.controller.search_patients()

    def buscar_patient(self):
        buscar=self.buscar.text()
        self.listPaciente=self.controller.search_patients(buscar)
        self.tableUpdate()

    def  agregar_patient(self):
        name = self.nombre.text()
        last_name = self.apellido.text()
        age = self.edad.text()
        id = self.id.text()
        if not id or not name or not last_name or not age:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Debe ingresar todos los datos")
            msgBox.setWindowTitle('Datos faltantes')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            pat = {'id':id, 'nombre':name, 'apellido': last_name, 'edad': age}
            isUnique = self.controller.add_patient(pat)
            if not isUnique:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("La id ya existe")
                msgBox.setWindowTitle('Id repetida')
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            else:
                self.readPacient()
                self.tableUpdate()
                self.id.setText('')
                self.nombre.setText('')
                self.apellido.setText('')
                self.edad.setText('')
    
    def tableUpdate(self):
        self.tabla.setRowCount(len(self.listPaciente)) 
        self.tabla.setColumnCount(5) 
        columnas = ["ID", "Nombre", "Apellido", "Edad", "Eliminar"]
        columnLayout = ['id','nombre','apellido','edad']
        self.tabla.setHorizontalHeaderLabels(columnas)
        for row, paciente in enumerate(self.listPaciente):
            for column in range(4):
                item = QTableWidgetItem(paciente[columnLayout[column]])
                self.tabla.setItem(row, column, item)
            
            btn = QPushButton('Borrar', self)
            btn.clicked.connect(lambda ch, r=row: self.Eliminar(r))
            self.tabla.setCellWidget(row, 4, btn)
                
        self.tabla.setColumnWidth(0, 80)  
        self.tabla.setColumnWidth(1, 110)  
        self.tabla.setColumnWidth(2, 60)  
        self.tabla.setColumnWidth(3, 60)  
        self.tabla.setColumnWidth(4, 60)

    def Eliminar(self, row):
        id = self.tabla.item(row, 0).text()
        deleted = self.controller.del_patient(id)
        if deleted:
            self.readPacient()
            self.tableUpdate()

    
       
def main():
    app = QApplication(sys.argv)
    vista_=VentanaIngreso()
    vista_.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

        


        